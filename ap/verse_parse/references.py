# adapted from python-scriptures

import re
import urllib2
import json

from bible_re import testaments, book_re, scripture_re

class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass

def get_book(name):
    """
    Get a book from its name or None if not found
    """
    for books in testaments.itervalues():
        for book in books:
            if re.match(book[2], name, re.IGNORECASE):
                return book
    return None

def extract(text):
    """
    Extract from a block of text a list of 2-tuples
    containing an outline point and a list of normalized, tupled verse references under that outline point.
    """
    outline = []
    for r in re.finditer(scripture_re, text):
        try:
            # find Roman numerals / outline points
            is_bullet = False
            for i in range(1,5): 
                if r.group(i):

                    outline.append({'string': r.group(i), 
                        'level': i, 
                        'refs': []})
                    is_bullet = True


            if is_bullet == False:

                # if no outline points yet, verses are from Scripture Reading
                if len(outline) == 0:
                    outline.append({'string': 'Scripture Reading', 
                        'level': 0, 
                        'refs': []})

                if r.group('book'): # reference contains book name
                    outline[-1]['refs'].append(normalize_reference(bookname=r.group('book'), chapter=r.group('chapter'), 
                                            verse=r.group('verse'), end_chapter=r.group('end_chapter'), end_verse=r.group('end_verse')))
                    if r.group('more_verses'): # reference contains multiple non-consecutive verse numbers
                        verses = extract_more_verses(r.group('more_verses')) # get extra verses in a list
                        for verse in verses: # append one reference for each extra verse
                           outline[-1]['refs'].append(normalize_reference(bookname=r.group('book'), chapter=r.group('chapter'), 
                                                 verse=verse[0], end_verse=verse[1]))
                else:
                    # get book from previous reference
                    i = -1
                    while len(outline[i]['refs']) == 0:
                        i -= 1
                    book = outline[i]['refs'][-1]['book']
                    if r.group('headless_chapter'): # headless reference
                        outline[-1]['refs'].append(normalize_reference(bookname=book, chapter=r.group('headless_chapter'),
                            verse=r.group('headless_verse'), end_chapter=r.group('headless_end_chapter'), end_verse=r.group('headless_end_verse')))
                        if r.group('more_headless_verses'):
                            verses = extract_more_verses(r.group('more_headless_verses'))
                            for verse in verses:
                                outline[-1]['refs'].append(normalize_reference(bookname=book, chapter=r.group('headless_chapter'), 
                                                 verse=verse[0], end_verse=verse[1]))
                    else:
                        if r.group('lonely_verse'):
                            i = -1
                            while len(outline[i]['refs']) == 0:
                                i -= 1
                            chapter = outline[i]['refs'][-1]['chapter']
                            outline[-1]['refs'].append(normalize_reference(bookname=book, chapter=chapter, verse=r.group('lonely_verse'), end_verse=r.group('lonely_end_verse')))

                            if r.group('more_lonely_verses'):
                                verses = extract_more_verses(r.group('more_lonely_verses'))
                                for verse in verses:
                                    outline[-1]['refs'].append(normalize_reference(bookname=book, chapter=chapter, verse=verse[0], end_verse=verse[1]))

        except InvalidReferenceException:
            pass
    return outline


def extract_more_verses(text):
    """
    Extract a list of verse numbers from a string of verse numbers, i.e. '3, 7, 10-14, 16'.
    Returns a list of tuples: (verse, end_verse,).
    e.g. '3, 7, 10-14, 16' --> [('3', '',), ('7', '',), ('10', '14',), ('16', '',)]
    """
    verses = re.findall(re.compile(r'(?P<verse>\d{1,3})(?:-(?P<end_verse>\d{1,3}))?'), text)
    return verses

def is_valid_reference(bookname, chapter, verse=None,
                                 end_chapter=None, end_verse=None, more_verses=None):
    """
    Check to see if a scripture reference is valid
    """
    try:
        return normalize_reference(bookname, chapter, verse,
            end_chapter, end_verse) is not None
    except InvalidReferenceException:
        return False

def reference_to_string(ref):
    '''
    Takes tupled verse reference (book, chapter, verse, end_chapter, end_verse)
    and formats verse reference as a string.
    e.g. ('John', 3, 16,) --> 'John 3:16'
    ('2 Cor.', 3, 16, 3, 18) --> '2 Cor. 3:16-18'
    '''
    if ref['chapter'] is not None:
        ref_string = ref['book'] + ' ' + str(ref['chapter']) + ':' + str(ref['verse'])
        if ref['end_chapter'] is not None:
            ref_string += '-'
            if ref['end_chapter'] == ref['chapter']:
                ref_string += str(ref['end_verse'])
            else:
                ref_string += str(ref['end_chapter']) + ':' + str(ref['end_verse'])
        return ref_string
    else:
        return ''

def normalize_reference(bookname=None, chapter=None, verse=None,
                                  end_chapter=None, end_verse=None):
    """
    Get a complete scripture reference with full book name
    from partial data.
    Reference is returned as a dictionary with keys:
    -book (book abbreviation)
    -chapter
    -verse
    -end_chapter
    -end_verse
    """
    book = get_book(bookname)

    # SPECIAL CASE FOR BOOKS WITH ONE CHAPTER:
    # If there is only one chapter in this book, set the chapter to one and
    # treat the incoming chapter argument as though it were the verse.
    # This normalizes references such as:
    # Jude 2 and Jude 2-4
    if len(book[3]) == 1:
        if verse is None and end_chapter is None:
            verse=chapter
            chapter=1
    else:
        # This is not a single chapter book.
        # If a start verse was NOT provided, but an end_verse was- we have a
        # reference such as John 3-4 which is invalid.
        if verse is None and end_verse:
            raise InvalidReferenceException()

    # Convert to integers or leave as None
    chapter = int(chapter) if chapter else None
    verse = int(verse) if verse else None
    end_verse = int(end_verse) if end_verse else None
    if end_verse is not None:
        end_chapter = int(end_chapter) if end_chapter else chapter

    # if (chapter < 1 or chapter > len(book[3])) \
    # or (verse is not None and (verse < 1 or verse > book[3][chapter-1])) \
    # or (end_chapter is not None and (
    #     end_chapter < 1
    #     or end_chapter < chapter
    #     or end_chapter > len(book[3]))) \
    # or (end_verse is not None and(
    #     end_verse < 1
    #     or (end_chapter and end_verse > book[3][end_chapter-1])
    #     or (chapter == end_chapter and end_verse < verse))):
    #     raise InvalidReferenceException()

    # if not verse:
    #     return (book[0], chapter, 1, chapter, book[3][chapter-1])
    # if not end_verse: 
    #     if end_chapter and end_chapter != chapter:
    #         end_verse = book[3][end_chapter-1]
    #     else:
    #         end_verse = verse
    # if not end_chapter:
    #     end_chapter = chapter

    return {'book': book[1], 
            'chapter': chapter,
            'verse': verse,
            'end_chapter': end_chapter,
            'end_verse': end_verse}
    # return (book[1], chapter, verse, end_chapter, end_verse)

def get_verses(ref):
    ''' 
    Returns a dictionary {reference: verse} of a verse (or multiple consecutive verses) 
    from a tupled verse reference (book, chapter, verse, end_chapter, end_verse)
    '''
    book_abbrev = ref['book'].strip('.').replace(' ', '')
    try: 
        if ref['end_chapter'] is None:
            response = urllib2.urlopen("http://rcvapi.herokuapp.com/v/%s/%d/%d" % (book_abbrev, ref['chapter'], ref['verse'],))
        else:
            response = urllib2.urlopen("http://rcvapi.herokuapp.com/vv/%s/%d/%d/%s/%d/%d" % (book_abbrev, ref['chapter'], ref['verse'], book_abbrev, ref['end_chapter'], ref['end_verse'],) )
        data = json.loads('[%s]' % response.read())
        verses = data[0]['verses']
        print(verses)
        return verses
    except:
        return {}

def find_repeat(outline, reference, i):
    '''
    Finds the first occurrence of the given reference in the outline, 
    from the beginning of the outline until outline[i].
    Returns False if there are no occurrences before outline[i], 
    otherwise returns the outline point of the first occurrence as a string (e.g. 'II.A.').
    '''
    for j in range(i):
        outline_pt = outline[j]
        for ref in outline_pt['refs']:
            if ref['book'] == reference['book']:
                if ref['chapter'] == reference['chapter']:
                    if ref['verse'] == reference['verse']:
                        if ref['end_chapter'] == reference['end_chapter']:
                            if ref['end_verse'] == reference['end_verse']:
                                repeat_point = outline_pt['string']

                                level = outline_pt['level']
                                k = j-1
                                while level > 1 and k >= 0:
                                    if outline[k]['level'] == level-1:
                                        repeat_point = outline[k]['string'].strip() + repeat_point
                                        level = outline[k]['level']
                                    k -= 1

                                return repeat_point
    return False
