-- Task 1 - select all the artists

SELECT Name FROM "Artists";

-- Task 2 - Count how many artists are there in the database

SELECT COUNT (*) AS "Numer Artists" FROM Artists;

-- Task 3 - Select the name of all tracks that are of the rock genre

SELECT Tracks.Name AS "Rock Tracks", Genres.Name AS "Genres"
FROM Tracks
JOIN Genres ON Tracks.GenreId = Genres.GenreId
WHERE Genres.Name LIKE "rock";


-- Task 4 - Select the name of all the tracks that are in MPEG audio file format

SELECT MediaTypes.Name AS "Type file",  Tracks.Name AS "Song name"
FROM Tracks
JOIN MediaTypes ON MediaTypes.MediaTypeId = Tracks.MediaTypeId
WHERE MediaTypes.Name LIKE "MPEG audio file";

-- Task 5 - Select all the tracks that are performed by Queen

SELECT Name, Composer AS "Preformer"
FROM Tracks
WHERE Composer LIKE "queen";

-- Task 6 - Select all the tracks that are in MPEG audio file format and are Pop genre

SELECT Tracks.Name AS "Тrack", MediaTypes.Name AS "Media type", Genres.Name AS "Genre"
FROM Tracks
JOIN Genres ON Genres.GenreId = Tracks.GenreId
JOIN MediaTypes ON MediaTypes.MediaTypeId = Tracks.MediaTypeId
WHERE Genres.Name LIKE "Pop" AND MediaTypes.Name LIKE "MPEG audio file";

-- Task 7 - Select the sum of the total quantity of sold tracks for "Let Me Love You Baby"

SELECT Tracks.Name AS "Song", SUM (InvoiceItems.Quantity) AS "Quantity"
FROM InvoiceItems
JOIN Tracks ON Tracks.TrackId = InvoiceItems.TrackId
WHERE Tracks.Name = "Let Me Love You Baby"

-- DONE --