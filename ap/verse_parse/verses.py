import urllib2
import json

# from docx import Document

from references import extract

def find_repeat(prev_refs, ref):
	return

def get_verses(ref):
	''' 
	Returns a dictionary {reference: verse} of a verse (or multiple consecutive verses) 
	from a tupled verse reference (book, chapter, verse, end_chapter, end_verse)
	'''
	book_abbrev = ref[0].strip('.').replace(' ', '')
	if ref[3] is None:
		response = urllib2.urlopen("http://rcvapi.herokuapp.com/v/%s/%d/%d" % (book_abbrev, ref[1], ref[2],))
	else:
		response = urllib2.urlopen("http://rcvapi.herokuapp.com/vv/%s/%d/%d/%s/%d/%d" % (book_abbrev, ref[1], ref[2], book_abbrev, ref[3], ref[4],) )
	data = json.loads('[%s]' % response.read())
	verses = data[0]['verses']
	return verses

def print_reference(ref):
	'''
	Takes tupled verse reference (book, chapter, verse, end_chapter, end_verse)
	and formats verse reference as a string.
	e.g. ('John', 3, 16,) --> 'John 3:16'
	('2 Cor.', 3, 16, 3, 18) --> '2 Cor. 3:16-18'
	'''
	if ref[1] is not None:
		ref_string = ref[0] + ' ' + str(ref[1]) + ':' + str(ref[2])
		if ref[3] is not None:
			ref_string += '-'
			if ref[3] == ref[1]:
				ref_string += str(ref[4])
			else:
				ref_string += str(ref[3]) + ':' + str(ref[4])
		return ref_string
	else:
		return ''

def make_document(outline):
	# outline = extract(text)
	document = Document()
	for outline_pt in outline:
		p = document.add_paragraph('')
		p.add_run(outline_pt[1]).bold = True

		for ref in outline_pt[2]:
			# check if verse appears earlier in outline
			is_repeat = False
			ref_string = ''
			for pt in outline:
				for r in pt[2]:
					if ref == r:
						is_repeat = True
						ref_string = '(See %s)' % pt[1]
			if is_repeat == False:
				ref_string = print_reference(ref)
			p.add_run(ref_string).bold = True
			document.add_paragraph('')

	document.save('verse_sheet.docx')
