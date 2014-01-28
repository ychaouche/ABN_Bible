import sqlite3
import xml.etree.ElementTree as xml
from string import replace

Project_Location = '/Volumes/Data/PyCharm_Projects/ABN_Bible'
Eng_Books_XML = Project_Location + '/bibles/Engilsh_BookNames.xml'
Bible_DB = Project_Location + '/database/bible.db'
KJV_Bible_XML = Project_Location + '/bibles/kjv.xml'
BSI_Tm_Bible_XML = Project_Location + '/bibles/tamil.xml'
AKJV_Bible_XML = Project_Location + '/bibles/akjv.xml'
UKJV_Bible_XML = Project_Location + '/bibles/ukjv.xml'
ASV_Bible_XML = Project_Location + '/bibles/asv.xml'
DARBY_Bible_XML = Project_Location + '/bibles/darby.xml'
AMP_Bible_XML = Project_Location + '/bibles/amp.xml'
#NSB_Bible_XML = Project_Location + '/bibles/nsb.xml'
CEV_Bible_XML = Project_Location + '/bibles/cev.xml'
ESV_Bible_XML = Project_Location + '/bibles/esv.xml'
#MSG_Bible_XML = Project_Location + '/bibles/msg.xml'
NASB_Bible_XML = Project_Location + '/bibles/nasb.xml'
NIV_Bible_XML = Project_Location + '/bibles/niv.xml'
#NKJV_Bible_XML = Project_Location + '/bibles/nkjv.xml'
#NLT_Bible_XML = Project_Location + '/bibles/nlt.xml'
#NRSV_Bible_XML = Project_Location + '/bibles/nrsv.xml'


def GetDBCursor():
    connection = sqlite3.connect(Bible_DB)
    cursor = connection.cursor()
    return connection, cursor


def CreateBooksTable():
    connection, cursor = GetDBCursor()
    cursor.execute("DROP TABLE IF EXISTS books;")
    cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY ASC, "
                   "eng_code TEXT, eng_short TEXT, eng_long TEXT, "
                   "tm_short TEXT)")
    connection.commit()
    cursor.close()


def GetEngBooks():
    tree = xml.parse(Eng_Books_XML)  # Parse the xml
    Eng_Books = list(tree.iter("book"))  # List of books
    del tree
    return Eng_Books


def InsertEngBooks():  # English Insert Rest Update
    connection, cursor = GetDBCursor()
    for book in GetEngBooks():
        Bname = book.get('short')
        abbr1 = book.get('code')
        abbr2 = book.get('abbr')  # Redundant
        Bname_ln = book.get('long')
        sql = "INSERT INTO books (eng_code, eng_short, eng_long) VALUES " \
              "('{0}', '{1}', '{2}');".format(abbr1, Bname, Bname_ln)
        cursor.execute(sql)
    connection.commit()
    cursor.close()


def GetTmBooks():
    tree = xml.parse(BSI_Tm_Bible_XML)
    Tm_Books = list(tree.find('booknames').text.split(','))
    del tree
    return Tm_Books


def AddTamilBooks():
    connection, cursor = GetDBCursor()
    for i, val in enumerate(GetTmBooks()):
        sql = "UPDATE books SET tm_short='".encode("UTF-8")
        sql = sql + val + "' WHERE id={0};".format(i + 1).encode("UTF-8")
        cursor.execute(sql)
    connection.commit()
    cursor.close()


def CreateKJV():
    connection, cursor = GetDBCursor()
    tree = xml.parse(KJV_Bible_XML)
    KJV_Books = list(tree.iter("b"))
    cursor.execute("DROP TABLE IF EXISTS kjv;")
    cursor.execute("CREATE TABLE kjv (book_id INTEGER, chapter_id INTEGER, "
                   "verse_id INTEGER, verse TEXT)")
    for i, Book in enumerate(KJV_Books):
        Chapters = list(Book.iter("c"))
        Bname = Book.get('n')
        for Chapter in Chapters:
            Verses = list(Chapter.iter("v"))
            Cno = int(Chapter.get('n'))
            print Bname, Cno
            for Verse in Verses:
                Vno = int(Verse.get('n'))
                sql = "INSERT INTO kjv (book_id, chapter_id, verse_id, verse) "\
                      """VALUES ({0}, {1}, {2}, "{3}");""".format(i+1, Cno, Vno,
                                                                  Verse.text)
                cursor.execute(sql)
    connection.commit()
    cursor.close()
    del tree


def CreateBSI_Tm():
    connection, cursor = GetDBCursor()
    tree = xml.parse(BSI_Tm_Bible_XML)
    cursor.execute("DROP TABLE IF EXISTS tamil;")
    cursor.execute("CREATE TABLE tamil (book_id INTEGER, chapter_id INTEGER, "
                   "verse_id INTEGER, verse TEXT)")
    Books = list(tree.iter("b"))
    for Book in Books:
        Chapters = list(Book.iter("c"))
        Bname = Book.get('bname')
        Bnumber = int(Book.get('bnumber'))
        for Chapter in Chapters:
            Verses = list(Chapter.iter("v"))
            Cno = int(Chapter.get('cnumber'))
            #print Bname, Cno
            for Verse in Verses:
                Vno = int(Verse.get('vnumber'))
                sql = "INSERT INTO tamil (book_id, chapter_id, verse_id, " \
                      "verse) VALUES ({0}, {1}, {2}, '"
                sql = sql.format(Bnumber, Cno, Vno).encode("UTF-8")
                sql = sql + Verse.text + "');".encode("UTF-8")
                cursor.execute(sql)
    connection.commit()
    cursor.close()
    del tree

def escapeString(verse):
    return replace(verse, '"', '""')

def CreateBible(bibleName, xmlPath, book='b', chapter='c', verse='v', name='n'):
    connection, cursor = GetDBCursor()
    tree = xml.parse(xmlPath)
    KJV_Books = list(tree.iter(book))
    cursor.execute("DROP TABLE IF EXISTS {0};".format(bibleName))
    cursor.execute("CREATE TABLE {0} (book_id INTEGER, chapter_id INTEGER, "
                   "verse_id INTEGER, verse TEXT)".format(bibleName))
    for i, Book in enumerate(KJV_Books):
        Chapters = list(Book.iter(chapter))
        Bname = Book.get(name)
        for Chapter in Chapters:
            Verses = list(Chapter.iter(verse))
            Cno = int(Chapter.get(name))
            #print Bname, Cno
            for Verse in Verses:
                try:
                    Vno = int(Verse.get(name))
                    sql = "INSERT INTO {4} (book_id, chapter_id, verse_id, verse) "\
                      """VALUES ({0}, {1}, {2}, "{3}");""".format(i+1, Cno, Vno,
                                                                  escapeString(Verse.text),
                                                                  bibleName)
                    cursor.execute(sql)
                except Exception as e:
                    print e
                    print bibleName, Bname, Cno, Vno, Verse.text, type(Verse.text)
                    print escapeString(Verse.text)
    connection.commit()
    cursor.close()
    del tree

def setupBibleDatabase():
    CreateBooksTable()
    InsertEngBooks()
    AddTamilBooks()
    CreateBible('kjv', KJV_Bible_XML)
    CreateBSI_Tm()
    CreateBible('akjv', AKJV_Bible_XML)
    CreateBible('ukjv', UKJV_Bible_XML)
    CreateBible('asv', ASV_Bible_XML)
    CreateBible('darby', DARBY_Bible_XML)
    CreateBible('amp', AMP_Bible_XML, 'book', 'chapter', 'verse', 'name')
    #CreateBible('nsb', NSB_Bible_XML)
    CreateBible('cev', CEV_Bible_XML, 'book', 'chapter', 'verse', 'name')
    CreateBible('esv', ESV_Bible_XML, 'book', 'chapter', 'verse', 'name')
    #CreateBible('msg', MSG_Bible_XML, 'book', 'chapter', 'verse', 'name')
    CreateBible('nasb', NASB_Bible_XML, 'book', 'chapter', 'verse', 'name')
    CreateBible('niv', NIV_Bible_XML, 'book', 'chapter', 'verse', 'name')
    #CreateBible('nkjv', NKJV_Bible_XML, 'book', 'chapter', 'verse', 'name')
    #CreateBible('nlt', NLT_Bible_XML, 'book', 'chapter', 'verse', 'name')
    #CreateBible('nrsv', NRSV_Bible_XML, 'book', 'chapter', 'verse', 'name')

if __name__ == '__main__':
    setupBibleDatabase()