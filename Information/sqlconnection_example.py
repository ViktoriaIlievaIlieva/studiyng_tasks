from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection, LegacyCursorResult

path_to_database = "C:\\Users\\capit\\Desktop\\Coding\\study.db"
engine: Engine = create_engine(f"sqlite:///{path_to_database}")

connection: Connection = engine.connect()

id = 3
cursor_to_result: LegacyCursorResult = connection.execute("""
SELECT * 
FROM Students 
WHERE ID = ?
""", id)

name = input("Enter name: ")
class_id = 3

connection.execute("""  
INSERT INTO Students(Name, ClassID)
VALUES (?, ?)
""", name, class_id)

# one line from the result as tuple
first_line: tuple = cursor_to_result.fetchone()

# the whole table as a list of tuples
all_results: list[tuple] = cursor_to_result.fetchall()

connection.close()

