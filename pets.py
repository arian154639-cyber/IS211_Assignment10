"""
I used "DROP TABLE IF EXISTS" because we were taught that in IS 361. I also broke up the code into
multiple lines because that is also how we did that in IS 361. I used "connection.close()" at the end
instead of the with block from the weekly readings because that too is something I learned while working
on an assignment for another course. I put the SQL code inside a string because that is how I did it in 
another course.
"""

import sqlite3
connection = sqlite3.connect("pets.db")
cursor = connection.cursor()

cursor.execute("""
DROP TABLE IF EXISTS person
""");

cursor.execute("""
DROP TABLE IF EXISTS pet
""");

cursor.execute("""
DROP TABLE IF EXISTS person_pet
""");

cursor.execute("""
CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
)
""");

cursor.execute("""
CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT, 
breed TEXT, 
age INTEGER, 
dead INTEGER
)
""");

cursor.execute("""
CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
)
""");

connection.commit()
connection.close()