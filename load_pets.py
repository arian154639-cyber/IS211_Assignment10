"""
I broke up the code into multiple lines because that is also how we did that in IS 361. I used 
"connection.close()" at the end instead of the with block from the weekly readings because that
too is something I learned while working on an assignment for another course. I put the SQL code 
inside a string because that is how I did it in another course.

To answer the question on what person_pet does, the answer is that it serves as the junction table
that is used to store the primary keys of the other two tables. This way, the two tables can be
connected. The weekly materials say that junction tables can be used for many-to-many relationships,
but in this case, it appears we have only one-to-one or one-to-many relationships (these other relationship
types were also covered in IS 361). 
"""

import sqlite3

def main():
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO person (id, first_name, last_name, age)
    VALUES (1, 'James', 'Smith', 41)
    """);

    cursor.execute("""
    INSERT INTO person (id, first_name, last_name, age)
    VALUES (2, 'Diana', 'Greene', 23)
    """);

    cursor.execute("""
    INSERT INTO person (id, first_name, last_name, age)
    VALUES (3, 'Sara', 'White', 27)
    """);

    cursor.execute("""
    INSERT INTO person (id, first_name, last_name, age)
    VALUES (4, 'William', 'Gibson', 23)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (1, 'Rusty', 'Dalmation', 4, 1)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (2, 'Bella', 'AlaskanMalamute', 3, 0)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (3, 'Max', 'CockerSpaniel', 1, 0)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (4, 'Rocky', 'Beagle', 7, 0)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (5, 'Rufus', 'CockerSpaniel', 1, 0)
    """);

    cursor.execute("""
    INSERT INTO pet (id, name, age, breed, dead)
    VALUES (6, 'Spot', 'Bloodhound', 2, 1)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (1, 1)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (1, 2)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (2, 3)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (2, 4)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (3, 5)
    """);

    cursor.execute("""
    INSERT INTO person_pet (person_id, pet_id)
    VALUES (4, 6)
    """);

    connection.commit()
    connection.close()

if __name__ == "__main__":
    print("Running load_pets.py")
    main()
