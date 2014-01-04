from CreateDB import Bible_DB
import sqlite3
import re
import string


class SQliteConnection():
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

eng_bks_long = {}
eng_bks_abb1 = {}
with SQliteConnection(Bible_DB) as c:
    c.execute("SELECT * from books")
    for book in c.fetchall():
        eng_bks_long[str(book[2])] = book[0]
        eng_bks_abb1[str(book[1])] = book[0]

def find(term, bible='kjv'):
    def getID(book, num=None):
        ids = []
        if not num:  # Books without number
            if book.upper() in eng_bks_abb1:  # Try abbreviation search
                return eng_bks_abb1[book.upper()]
            else:  # Book without number and Failed abb search
                for x in eng_bks_long:
                    if all([i in x.lower() for i in bk.lower()]):
                        #print "Found!", x, eng_bks_long[x]
                        ids.append(eng_bks_long[x])
                return min(ids)
        else:  # Books with numbers
            combine = str(num)+book
            if combine.upper() in eng_bks_abb1:  # Try abbreviation search
                return eng_bks_abb1[combine.upper()]
            else:  # Book with number and Failed abb search
                for x in eng_bks_long:
                    if all([i in x.lower() for i in bk.lower()]) and num in x:
                        #print "Found!", x, eng_bks_long[x]
                        ids.append(eng_bks_long[x])
                return min(ids)

    def getScripture(id, chapter, verse=None, end=None):
        with SQliteConnection(Bible_DB) as c:
            if not verse and not end: # No verse and end specified
                sql = "SELECT verse_id, verse from {0} where book_id={1} and " \
                      "chapter_id={2};"
                sql = sql.format(bible, id, chapter)
                c.execute(sql)
                return c.fetchall()
            if verse and not end:
                sql = "SELECT verse_id, verse from {0} where book_id={1} and " \
                      "chapter_id={2} and verse_id={3};"
                sql = sql.format(bible, id, chapter, verse)
                c.execute(sql)
                return c.fetchone()
            if verse and end:
                sql = "SELECT verse_id, verse from {0} where book_id={1} and " \
                      "chapter_id={2} and verse_id between {3} and {4};"
                sql = sql.format(bible, id, chapter, verse, end)
                c.execute(sql)
                return c.fetchall()

    term_split = bsSplit(term)
    if term_split:  # Check for None
        if term_split[0].startswith(tuple(string.digits)):  # Starts with Digits
            if len(term_split) == 5:  # Yes Num, Yes Dash
                bknum, bk, chap, verse, end = term_split
                #print bknum, bk, chap, verse, end
                bkid = getID(bk, bknum)
                if bkid:
                    return getScripture(bkid, chap, verse, end)
            elif len(term_split) == 4: # Yes Num, No Dash
                bknum, bk, chap, verse = term_split
                #print bknum, bk, chap, verse
                #print getID(bk, bknum)
                bkid = getID(bk, bknum)
                if bkid:
                    return getScripture(bkid, chap, verse)
            elif len(term_split) == 3:  # Only Bk, Chap
                bknum, bk, chap = term_split
                #print bknum, bk, chap
                bkid = getID(bk, bknum)
                if bkid:
                    return getScripture(bkid, chap)
        else:                                               # No Digits
            if len(term_split) == 4:  # No Num, Yes Dash
                bk, chap, verse, end = term_split
                #print bk, chap, verse, end
                #print getID(bk)
                bkid = getID(bk)
                if bkid:
                    return getScripture(bkid, chap, verse, end)
            elif len(term_split) == 3:  # No Num, No Dash
                bk, chap, verse = term_split
                #print bk, chap, verse
                #print getID(bk)
                bkid = getID(bk)
                if bkid:
                    return getScripture(bkid, chap, verse)
            elif len(term_split) == 2:  # Only Bk, Chap
                bk, chap = term_split
                #print bk, chap
                #print getID(bk)
                bkid = getID(bk)
                if bkid:
                    return getScripture(bkid, chap)
    else:
        #print "Not Found!"
        return None

def bsSplit(term):  # Returns None for invalid term
    if term.startswith(tuple(string.digits)):
        if '-' in term:
            match = re.match(r"([0-9]+)([a-z]+)([0-9]+):([0-9]+)-([0-9]+)",
                             term, re.I)
            if match:
                items = match.groups()
                return items
        elif ':' in term:
            match = re.match(r"([0-9]+)([a-z]+)([0-9]+):([0-9]+)", term, re.I)
            if match:
                items = match.groups()
                return items
        else:
            match = re.match(r"([0-9]+)([a-z]+)([0-9]+)", term, re.I)
            if match:
                items = match.groups()
                return items
    else:
        if '-' in term:
            match = re.match(r"([a-z]+)([0-9]+):([0-9]+)-([0-9]+)", term, re.I)
            if match:
                items = match.groups()
                return items
        elif ':' in term:
            match = re.match(r"([a-z]+)([0-9]+):([0-9]+)", term, re.I)
            if match:
                items = match.groups()
                return items
        else:
            match = re.match(r"([a-z]+)([0-9]+)", term, re.I)
            if match:
                items = match.groups()
                return items

#-----------Books with Number and Chapter
# x = find('1jn2')
# for i in x: print i[0], i[1]
#-----------Books with Number and Chapter and Verse
#y = find('1jn1:1')
#print y[0], y[1]
#-----------Books with Number and Chapter and Verse Range
#z = find('1jn1:1-3')
#for i in z: print i[0], i[1]
#-----------Book Chapter
#for i in find('gen1'): print i[0], i[1]
#-----------Book Chapter Verse
#print find('gen1:1')
#-----------Book Chapter Verse Range
#for i in find('jhn3:15-17'): print i[0], i[1]
