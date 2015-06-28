""" bibleBook.py
The BibleBook is a dictionary class that is used to store the 
books from the Bible and the content of those books (name, chapters, verses).

"""
class BibleBook:
	BIBLE_BOOKS = (
  ('01_GEN', 'Genesis', 50, 1533),
  ('02_EXO', 'Exodus', 40, 1213),
  ('03_LEV', 'Leviticus', 27, 859),
  ('04_NUM', 'Numbers', 36, 1288),
  ('05_DEUT', 'Deuteronomy', 34, 959),
  ('06_JOSH', 'Joshua', 24, 658),
  ('07_JUDGE', 'Judges', 21, 618),
  ('08_RUTH', 'Ruth', 4, 85),
  ('09_1SAM', '1 Samuel', 31, 810),
  ('10_2SAM', '2 Samuel', 24, 695),
  ('11_1KINGS', '1 Kings', 22, 816),
  ('12_2KINGS', '2 Kings', 25, 719),
  ('13_1CHRON', '1 Chronicles', 29, 942),
  ('14_2CHRON', '2 Chronicles', 36, 822),
  ('15_EZRA', 'Ezra', 10, 280),
  ('16_NEH', 'Nehemiah', 13, 406),
  ('17_ESTH', 'Esther', 10, 167),
  ('18_JOB', 'Job', 42, 1070),
  ('19_PSA', 'Psalms', 150, 2461),
  ('20_PROV', 'Proverbs', 31, 915),
  ('21_ECCL', 'Ecclesiastes', 12, 222),
  ('22_SS', 'Song of Songs', 8, 117),
  ('23_ISA', 'Isaiah', 66, 1292),
  ('24_JER', 'Jeremiah', 52, 1364),
  ('25_LAM', 'Lamentations', 5, 154),
  ('26_EZEK', 'Ezekiel', 48, 1273),
  ('27_DAN', 'Daniel', 12, 357),
  ('28_HOSEA', 'Hosea', 14, 197),
  ('29_JOEL', 'Joel', 3, 73),
  ('30_AMOS', 'Amos', 9, 146),
  ('31_OBAD', 'Obadiah', 1, 21),
  ('32_JONAH', 'Jonah', 4, 48),
  ('33_MICAH', 'Micah', 7, 105),
  ('34_NAHUM', 'Nahum', 3, 47),
  ('35_HAB', 'Habakkuk', 3, 56),
  ('36_ZEPH', 'Zephaniah', 3, 53),
  ('37_HAG', 'Haggai', 2, 38),
  ('38_ZECH', 'Zechariah', 14, 211),
  ('39_MAL', 'Malachi', 4, 55),
  ('40_MATT', 'Matthew', 28, 1071),
  ('41_MARK', 'Mark', 13, 678),
  ('42_LUKE', 'Luke', 24, 1151),
  ('43_JOHN', 'John', 21, 879),
  ('44_ACTS', 'Acts', 28, 1007),
  ('45_ROM', 'Romans', 16, 433),
  ('46_1COR', '1 Corinthians', 16, 437),
  ('47_2COR', '2 Corinthians', 13, 257),
  ('48_GAL', 'Galatians', 6, 149),
  ('49_EPH', 'Ephesians', 6, 155),
  ('50_PHIL', 'Philippians', 4, 104),
  ('51_COL', 'Colossians', 4, 95),
  ('52_1THES', '1 Thessalonians', 5, 89),
  ('53_2THES', '2 Thessalonians', 3, 47),
  ('54_1TIM', '1 Timothy', 6, 113),
  ('55_2TIM', '2 Timothy', 4, 83),
  ('56_TITUS', 'Titus', 3, 46),
  ('57_PHILEM', 'Philemon', 1, 25),
  ('58_HEB', 'Hebrews', 13, 303),
  ('59_JAMES', 'James', 5, 108),
  ('60_1PET', '1 Peter', 5, 105),
  ('61_2PET', '2 Peter', 3, 61),
  ('62_1JOHN', '1 John', 5, 105),
  ('63_2JOHN', '2 John', 1, 13),
  ('64_3JOHN', '3 John', 1, 15),
  ('65_JUDE', 'Jude', 1, 25),
  ('66_REV', 'Revelation', 22, 404),
  )

	def get_verses(self, book):
		for i in range (0, len(self.BIBLE_BOOKS)):
			if book in self.BIBLE_BOOKS[i][0]:
				return self.BIBLE_BOOKS[i][3]
			elif book in self.BIBLE_BOOKS[i][1]:
				return self.BIBLE_BOOKS[i][3]

	def get_chapters(self, book):
		for i in range (0, len(self.BIBLE_BOOKS)):
			if book in self.BIBLE_BOOKS[i][0]:
				return self.BIBLE_BOOKS[i][2]
			elif book in self.BIBLE_BOOKS[i][1]:
				return self.BIBLE_BOOKS[i][2]

	def get_book(self, book):
		for i in range (0, len(self.BIBLE_BOOKS)):
			if book in self.BIBLE_BOOKS[i][0]:
				return self.BIBLE_BOOKS[i][1]
			elif book in self.BIBLE_BOOKS[i][1]:
				return self.BIBLE_BOOKS[i][1]

	def get_book_by_index(self, index):
		if index < len(self.BIBLE_BOOKS):
			return self.BIBLE_BOOKS[index][1]

