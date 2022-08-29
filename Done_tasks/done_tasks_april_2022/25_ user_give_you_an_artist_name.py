# Task 2 - Using the chinook database... ask the user to give you an artist name and print only the track name
# for each track that has that composer.

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection, LegacyCursorResult
from thefuzz import fuzz

artist: str = input("Enter artist: ")
path_database = "C:\\Users\\capit\\Desktop\\Coding\\chinook.db"
engine: Engine = create_engine(f"sqlite:///{path_database}")
connection: Connection = engine.connect()
cursor: LegacyCursorResult = connection.execute('''
SELECT Name
FROM Tracks
WHERE Composer lIKE ?;
''', artist)
all_results: list[tuple] = cursor.fetchall()
connection.close()
for track in all_results:
    print(track[0])
