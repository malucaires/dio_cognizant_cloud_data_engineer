CREATE DATABASE yt

USE yt

CREATE TABLE videos(
	id_video INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(30),
    title VARCHAR(30),
    likes INT,
    dislikes INT
)

INSERT INTO videos (author, title, likes, dislikes) VALUES ('Maria', 'MySQL', 10, 2);
INSERT INTO videos (author, title, likes, dislikes) VALUES ('João', 'HTML', 30, 1);
INSERT INTO videos (author, title, likes, dislikes) VALUES ('Maria', 'CSS', 18, 3);
INSERT INTO videos (author, title, likes, dislikes) VALUES ('Pedro', 'JavaScript', 15, 8);
INSERT INTO videos (author, title, likes, dislikes) VALUES ('Maria', 'Python', 50, 0);

CREATE TABLE author(
	id_author INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(30),
    born DATE    
)

INSERT INTO author (author, born) VALUES ('Maria', '1992-04-19');
INSERT INTO author (author, born) VALUES ('Pedro', '2000-10-12');
INSERT INTO author (author, born) VALUES ('João', '1998-03-09');
INSERT INTO author (author, born) VALUES ('Flávia', '2000-12-05')

UPDATE videos SET author = 1 WHERE id_video = 1;
UPDATE videos SET author = 3 WHERE id_video = 2;
UPDATE videos SET author = 1 WHERE id_video = 3;
UPDATE videos SET author = 2 WHERE id_video = 4;
UPDATE videos SET author = 1 WHERE id_video = 5

ALTER TABLE videos MODIFY COLUMN author INT

ALTER TABLE videos ADD CONSTRAINT fk_author FOREIGN KEY (author) REFERENCES author(id_author)

SELECT * FROM videos JOIN author ON videos.author = author.id_author

SELECT videos.title, author.author FROM videos JOIN author ON videos.author = author.id_author

CREATE TABLE seo(
	id_seo INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(20)
)

INSERT INTO videos (author, title, likes, dislikes) VALUES (2, 'PHP', 20, 8)

INSERT INTO seo (categoria) VALUES ('Frontend');
INSERT INTO seo (categoria) VALUES ('Backend')  

ALTER TABLE videos ADD fk_seo INT NOT NULL AFTER title

UPDATE videos SET fk_seo=1 WHERE id_video = 2;
UPDATE videos SET fk_seo=1 WHERE id_video = 3;
UPDATE videos SET fk_seo=1 WHERE id_video = 4;
UPDATE videos SET fk_seo=2 WHERE id_video = 1;
UPDATE videos SET fk_seo=2 WHERE id_video = 5;
UPDATE videos SET fk_seo=2 WHERE id_video = 6;

ALTER TABLE videos ADD CONSTRAINT fk_seo FOREIGN KEY (fk_seo) REFERENCES seo(id_seo)

SELECT videos.title, seo.categoria FROM videos JOIN seo ON videos.fk_seo = seo.id_seo

SELECT videos.title, author.author, seo.categoria FROM videos JOIN seo ON videos.fk_seo = seo.id_seo
JOIN author ON videos.author = author.id_author

CREATE TABLE playlist(
	id_video INT AUTO_INCREMENT PRIMARY KEY,
    name_pl VARCHAR(20)
)

INSERT INTO playlist (name_pl) VALUES ('HTML + CSS');
INSERT INTO playlist (name_pl) VALUES ('HTML + PHP + JS');
INSERT INTO playlist (name_pl) VALUES ('Pyhton + PHP')

CREATE TABLE videos_playlist(
	id_vp INT AUTO_INCREMENT PRIMARY KEY,
    fk_videos INT,
    fk_playlist int
)

INSERT INTO videos_playlist (fk_videos, fk_playlist) VALUES (2, 1);
INSERT INTO videos_playlist (fk_videos, fk_playlist) VALUES (3, 1)

SELECT playlist.name_pl, videos.title, author.author FROM playlist 
JOIN videos_playlist ON playlist.id_video = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos
JOIN author ON videos.author = author.id_author
