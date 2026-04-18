"""
I broke up the code into multiple lines because that is also how we did that in IS 361. I used 
"connection.close()" at the end instead of the with block from the weekly readings because that
too is something I learned while working on an assignment for another course. I used if/elif/else
for this script because we needed to handle -1 entires, non-numeric entries, and valid entires. 
This implementation is basic, there was another method but I thought this was fine. 
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
            print("Please try again.")
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
            print("Please try again.")

if __name__ == "__main__":
    print("Running query_pets.py")
    main()