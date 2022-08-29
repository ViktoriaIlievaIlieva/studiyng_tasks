# Task 3 - Using the study database create a program that will control the teachers.
# Ask for a command until a "quit" command is given.
# If the command is "add" you will be asked for a name for a new teacher and add that teacher to the database.
# If the command is "list" print all the teachers in the database and their IDs.
# If the command is "remove" - ask for an ID and delete the teacher with that ID.
# If the command is "update" then ask for an ID and a new name and update the teacher name with that ID.
# (The four commands are commonly known as CRUD = Create, Read, Update, Delete and are used quite often in any project)

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection, LegacyCursorResult
from thefuzz import fuzz

path_database: str = "C:\\Users\\capit\\Desktop\\Coding\\study.db"
engine: Engine = create_engine(f"sqlite:///{path_database}")
connection: Connection = engine.connect()

command: str = input("Enter command:\n 1. Add \n 2. List \n 3. Remove \n 4. Update \n 5. Quit: ")
while fuzz.ratio(command, "Quit") <= 80:

    if fuzz.ratio(command, "Add") >= 60:
        new_teacher: str = input("Add new teacher`s name: ")
        connection.execute("""
        INSERT INTO "Teachers" (Name)
        VALUES (?);
        """, new_teacher)

    elif fuzz.ratio(command, "List") >= 60:
        cursor_result: LegacyCursorResult = connection.execute("""
        SELECT Id, Name
        FROM Teachers; 
        """)
        all_results: list[tuple] = cursor_result.fetchall()
        for teacher in all_results:
            print(teacher[0], end=" ")
            print(teacher[1])

    elif fuzz.ratio(command, "Remove") >= 60:
        teacher_id = input("Insert id of teacher for removal: ")
        connection.execute("""
                DELETE FROM Teachers
                WHERE Id = ?;
                """, teacher_id)

    elif fuzz.ratio(command, "Update") >= 80:
        ch_id_teacher = input("Insert the ID where information should be changed: ")
        new_teacher_name = input("Insert new teacher`s name: ")
        connection.execute("""
                        UPDATE Teachers
                        SET
                        Name = ?
                        WHERE Id = ?;
                        """, new_teacher_name, ch_id_teacher)

    command: str = input("Enter command:\n 1. Add \n 2. List \n 3. Remove \n 4. Update \n 5. Quit: ")

connection.close()

