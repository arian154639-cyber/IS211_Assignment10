/* I used "DORP TABLE IF EXISTS" because we were taught that in IS 361. I included a junction table
   because the second and third part of the assignmnet used that strucutre, but you could also just
   map relationships through the id values, that's what I did in another course's assignment. */

DROP TABLE IF EXISTS artist:
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS song; 

CREATE TABLE artist (
artist_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT);

CREATE TABLE album (
album_id INTEGER PRIMARY KEY,
album_name TEXT,
FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
);

CREATE TABLE song (
song_id INTEGER PRIMARY KEY,
song_name TEXT,
song_number INTEGER
song_duration TEXT,
FOREIGN KEY (album_id) REFERENCES album (album_id)
);

CREATE TABLE junction_table (
artist_id INTEGER,
album_id INTEGER,
song_id INTEGER,
FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
FOREIGN KEY (album_id) REFERENCES album (album_id)
FOREIGN KEY (song_id) REFERENCES song (song_id)
);
