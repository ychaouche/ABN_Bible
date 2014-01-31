import sqlite3
import xml.etree.ElementTree as xml
from string import replace

#Project_Location = '/Applications/ABN_Bible'
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
CEV_Bible_XML = Project_Location + '/bibles/cev.xml'
ESV_Bible_XML = Project_Location + '/bibles/esv.xml'
NASB_Bible_XML = Project_Location + '/bibles/nasb.xml'
NIV_Bible_XML = Project_Location + '/bibles/niv.xml'
NKJV_Bible_XML = Project_Location + '/bibles/nkjv.xml'
MSG_Bible_XML = Project_Location + '/bibles/msg.xml'
NLT_Bible_XML = Project_Location + '/bibles/nlt.xml'
NRSV_Bible_XML = Project_Location + '/bibles/nrsv.xml'
CH_NCVS_XML = Project_Location + '/bibles/ncv_simplified.xml'
CH_NCVT_XML = Project_Location + '/bibles/ncv_trad.xml'
ARABIC_XML = Project_Location + '/bibles/arabic.xml'
PERSIAN_XML = Project_Location + '/bibles/persian.xml'
DARI_XML = Project_Location + '/bibles/dari.xml'
RUSSIAN_XML = Project_Location + '/bibles/russian.xml'
RUSSIAN_SYN_XML = Project_Location + '/bibles/rus_synodal.xml'


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


def GetBooks(xmlFile, bookname):
    tree = xml.parse(xmlFile)
    Tm_Books = list(tree.find(bookname).text.split(','))
    del tree
    Tm_Books = [i.strip().replace('"','') if '"' in i else i for i in Tm_Books]
    return Tm_Books


def AddBooks(xmlFile, language, bookname='booknames', alter=False):
    connection, cursor = GetDBCursor()
    if alter:
        sql = 'ALTER TABLE books ADD COLUMN {0}'.format(language)
        cursor.execute(sql)
    for i, val in enumerate(GetBooks(xmlFile, bookname)):
        sql = "UPDATE books SET {0}='".format(language).encode("UTF-8")
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

def CreateBible_Unicode(language, bible, book="b", chapter="c", verse="v",
                        bname='n', cname='n', vname='n', escape=False):
    connection, cursor = GetDBCursor()
    tree = xml.parse(bible)
    cursor.execute("DROP TABLE IF EXISTS {0};".format(language))
    cursor.execute("CREATE TABLE {0} (book_id INTEGER, chapter_id INTEGER, "
                   "verse_id INTEGER, verse TEXT)".format(language))
    Books = list(tree.iter(book))
    for i, Book in enumerate(Books):
        Chapters = list(Book.iter(chapter))
        Bnumber = i+1
        cursor.execute("SELECT eng_short from books where id={0}".format(Bnumber))
        Bname = cursor.fetchone()[0]
        for Chapter in Chapters:
            Verses = list(Chapter.iter(verse))
            Cno = int(Chapter.get(cname))
            #print Bnumber, Cno
            for Verse in Verses:
                #print Verse.text
                Vno = int(Verse.get(vname))
                #print Bname, str(Cno)+':'+str(Vno)
                if escape:
                    vtext = escapeString(Verse.text)
                else:
                    vtext = Verse.text
                sql = "INSERT INTO {0} (book_id, chapter_id, verse_id, ".format(language)
                sql = sql + "verse) VALUES ({0}, {1}, {2}, '"
                sql = sql.format(Bnumber, Cno, Vno).encode("UTF-8")
                sql = sql + vtext + "');".encode("UTF-8")
                try:
                    cursor.execute(sql)
                except:
                    print sql
    connection.commit()
    cursor.close()
    del tree

def escapeString(verse):
    if '"' in verse:
        return replace(verse, '"', '""')
    elif "'" in verse:
        return replace(verse, "'", "''")
    else: return verse

def CreateBible(bibleName, xmlPath, book='b', chapter='c', verse='v', bname='n',
                cname='n', vname='n'):
    connection, cursor = GetDBCursor()
    tree = xml.parse(xmlPath)
    KJV_Books = list(tree.iter(book))
    cursor.execute("DROP TABLE IF EXISTS {0};".format(bibleName))
    cursor.execute("CREATE TABLE {0} (book_id INTEGER, chapter_id INTEGER, "
                   "verse_id INTEGER, verse TEXT)".format(bibleName))
    for i, Book in enumerate(KJV_Books):
        Chapters = list(Book.iter(chapter))
        Bname = Book.get(bname)
        for Chapter in Chapters:
            Verses = list(Chapter.iter(verse))
            Cno = int(Chapter.get(cname))
            #print Bname, Cno
            for Verse in Verses:
                try:
                    Vno = int(Verse.get(vname))
                    #print bibleName, Bname, Cno, Vno
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
    CreateBible('kjv', KJV_Bible_XML)
    AddBooks(BSI_Tm_Bible_XML, 'tm_short')
    CreateBible_Unicode('tamil', BSI_Tm_Bible_XML, bname='bnumber',
                        cname='cnumber', vname='vnumber')
    CreateBible('akjv', AKJV_Bible_XML)
    CreateBible('ukjv', UKJV_Bible_XML)
    CreateBible('asv', ASV_Bible_XML)
    CreateBible('darby', DARBY_Bible_XML)
    CreateBible('amp', AMP_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    #CreateBible('cev', CEV_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('esv', ESV_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('nasb', NASB_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('niv', NIV_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('nkjv', NKJV_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('msg', MSG_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('nlt', NLT_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    CreateBible('nrsv', NRSV_Bible_XML, 'book', 'chapter', 'verse', 'name', 'name', 'name')
    AddBooks(CH_NCVS_XML,'ch_ncvs', alter=True)
    CreateBible_Unicode('ch_ncvs', CH_NCVS_XML)
    AddBooks(CH_NCVT_XML,'ch_ncvt', alter=True)
    CreateBible_Unicode('ch_ncvt', CH_NCVT_XML)
    AddBooks(ARABIC_XML,'arabic', alter=True)
    CreateBible_Unicode('arabic', ARABIC_XML, bname='bnumber', cname='cnumber',
                        vname='vnumber')
    CreateBible_Unicode('persian', PERSIAN_XML, escape=True)
    CreateBible_Unicode('dari', DARI_XML, escape=True)
    AddBooks(RUSSIAN_XML,'russian', alter=True)
    CreateBible_Unicode('russian', RUSSIAN_XML)
    # AddBooks(RUSSIAN_SYN_XML,'rus_synodal', alter=True)  #  -- Duplicate Rus
    CreateBible_Unicode('rus_synodal', RUSSIAN_SYN_XML, bname='bnumber',
                        cname='cnumber', vname='vnumber')

if __name__ == '__main__':
    setupBibleDatabase()