"""
I broke up the code into multiple lines because that is also how we did that in IS 361. I used 
if/elif/else for this script because I determined we needed to handle -1 entires, non-numeric 
entries, and valid entires. This implementation is simple, there was another method but I thought 
this was fine. I put the SQL code inside a string because that is how I did it in another course.

Note: Refactored to have "connection.close()", which was used for closing the connection as I learned
that in another course. I forgot to include that in the original version. I also did type conversion 
in the refactor because this was a small script but I removed that. I sent an email on May 15th about
refactoring this assignment.
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
            """, (user_input,))

            data = cursor.fetchall()

            if data:
                print(data)
            else:
                print("No results.")

    connection.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    main()