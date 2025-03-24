Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
... 
... # Connect to SQLite database (or create it if it doesn't exist)
... conn = sqlite3.connect("tennisclub.db")
... cursor = conn.cursor()
... 
... # Create table
... cursor.execute('''
...     CREATE TABLE IF NOT EXISTS member (
...         ID INTEGER PRIMARY KEY AUTOINCREMENT,
...         Firstname TEXT NOT NULL,
...         Surname TEXT NOT NULL,
...         DateOfBirth DATE NOT NULL,
...         MemberType TEXT CHECK(MemberType IN ('Junior', 'Intermediate', 'Senior')) NOT NULL
...     )
... ''')
... 
... # Insert test data
... members = [
...     ("Alice", "Smith", "2008-05-14", "Junior"),
...     ("Bob", "Johnson", "1995-09-23", "Intermediate"),
...     ("Charlie", "Brown", "1980-11-02", "Senior"),
...     ("Diana", "White", "2005-07-19", "Junior"),
...     ("Edward", "Davis", "1992-03-30", "Intermediate"),
...     ("Fiona", "Clark", "1975-12-25", "Senior")
... ]
... 
... cursor.executemany("INSERT INTO member (Firstname, Surname, DateOfBirth, MemberType) VALUES (?, ?, ?, ?)", members)
... # Commit changes and close connection
