# Task 1 - Using the chinook database print only the name of all the artists each on a new line.

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection, LegacyCursorResult

path_to_database = "C:\\Users\\capit\\Desktop\\Coding\\chinook.db"

engine: Engine = create_engine(f"sqlite:///{path_to_database}")
connection: Connection = engine.connect()

cursor_to_result: LegacyCursorResult = connection.execute('''
SELECT Composer
FROM Tracks;
''')
all_results: list[tuple] = cursor_to_result.fetchall()
connection.close()
for index in all_results:
    print(index[0])

