-- Task 8 - Marketing needs to make a separation between HipHop and Rap so  -
-- Update the "Genre" "Hip Hop/Rap" to be just "Hip Hop" and insert a new genre called "Rap"
-- DONE
-- Task 9 - Update the quantity of each sold invoice item for the track "Dog Eat Dog" to be equal to 2
-- DONE
-- Task 10 - GDPR sails we cannot store the address anymore - clear all the values from the Customers table "Address" column
-- Done
-- Task 11 - Delete the Track "Dog Eat Dog" from any playlist (delete the link in PlaylistTrack table)

DELETE FROM PlaylistTrack
WHERE TrackId IN(
	SELECT TrackId
	FROM Tracks
	WHERE Tracks.Name = "Dog Eat Dog"
	);

-- Task 12 - Increase the Unit Price of all tracks that from the "Protected AAC audio file" media type by 2.5 dollars

UPDATE InvoiceItems
SET
UnitPrice = UnitPrice + 2.5
WHERE TrackId  IN (
	SELECT TrackId
	FROM Tracks
	JOIN MediaTypes ON MediaTypes.MediaTypeId = Tracks.MediaTypeId
	WHERE MediaTypes.Name = "Protected AAC audio file"
	);

-- Task 13 - Delete the tracks that are from the "Protected AAC audio file" media type from any playlist

DELETE FROM PlaylistTrack
WHERE TrackId IN(
	SELECT TrackId
	FROM Tracks
	JOIN MediaTypes ON MediaTypes.MediaTypeId = Tracks.MediaTypeId
	WHERE MediaTypes.Name = "Protected AAC audio file"
	);


DONE