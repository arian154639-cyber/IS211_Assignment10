/* I used "DROP TABLE IF EXISTS" because we were taught that in IS 361. I included a junction table
   because the second and third part of the assignmnet used that strucutre, but you could also just
   map relationships through the id values, that's what I did in another course's assignment. I left
   "DROP SCHEMA IF EXISTS" or "CREATE SCHEMA" or "USE SCHEMA" because I was unsure if those were 
   appropriate here. */

DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS song; 
DROP TABLE IF EXISTS junction_table;

CREATE TABLE artist (
artist_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT);

CREATE TABLE album (
album_id INTEGER PRIMARY KEY,
album_name TEXT
);

CREATE TABLE song (
song_id INTEGER PRIMARY KEY,
song_name TEXT,
song_number INTEGER,
song_duration TEXT
);

CREATE TABLE junction_table (
artist_id INTEGER,
album_id INTEGER,
song_id INTEGER
);
