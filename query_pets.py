"""
I broke up the code into multiple lines because that is also how we did that in IS 361. I used 
"connection.close()" at the end instead of the with block from the weekly readings because that
too is something I learned while working on an assignment for another course. I used if/elif/else
for this script because we needed to handle -1 entires, non-numeric entries, and valid entires. 
This implementation is basic, there was another method but I thought this was fine. I put the SQL 
code inside a string because that is how I did it in another course.

Note: Refactored to do type conversion and close connections. I did type conversion here because it's
a small assignment so type conversion in just one place doesn't take long to implement.
"""

import sqlite3

def main():
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    while True:
        user_input = input("Enter Person_ID: ")

        if user_input == "-1":
            break
        elif not user_input.isdigit():
            print("Input must be a number.")
            continue
        else:
            person_id = int(user_input)
            cursor.execute ("""
            SELECT
            person.first_name,
            person.last_name,
            person.age,
            pet.name,
            pet.breed,
            pet.age,
            pet.dead
            FROM person
            JOIN person_pet ON person.id = person_pet.person_id
            JOIN pet ON pet.id = person_pet.pet_id
            WHERE person.id = ?
            """, (person_id,))

            data = cursor.fetchall()

            if data:
                print(data)
            else:
                print("No results.")

    connection.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    main()