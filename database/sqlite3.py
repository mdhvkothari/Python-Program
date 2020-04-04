import sqlite3
MySchool = sqlite3.connect('schooltest.db')
cursorSchool = MySchool.cursor()

cursorSchool.execute('''CREATE TABLE student (
    Student ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL,
    age INTEGER,
    marks REAL);
''')

MySchool.close()
