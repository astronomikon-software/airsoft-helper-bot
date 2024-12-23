DROP TABLE places;
DROP TABLE groups;
DROP TABLE genres;
DROP TABLE users;
DROP TABLE matches;
DROP TABLE user_bot_states;
DROP TABLE subscriptions;

SET client_encoding TO 'UTF8';

CREATE TABLE places(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    place_name VARCHAR NOT NULL
);

CREATE TABLE groups(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    group_name VARCHAR NOT NULL
);

CREATE TABLE genres(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    genre_name VARCHAR NOT NULL
);

CREATE TABLE users(
    id BIGINT NOT NULL PRIMARY KEY,
    is_admin BOOLEAN NOT NULL,
    is_true_admin BOOLEAN NOT NULL
);

CREATE TABLE user_bot_states(
    user_id BIGINT NOT NULL PRIMARY KEY,
    state_json VARCHAR NOT NULL
);

CREATE TABLE matches(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    match_name VARCHAR NOT NULL,
    start_time TIMESTAMP NOT NULL,
    duration VARCHAR NOT NULL,
    place_name VARCHAR NOT NULL,
    group_id INT[] NOT NULL,
    genre_id INT[] NOT NULL,
    is_loneliness_friendly BOOLEAN NOT NULL,
    url VARCHAR NOT NULL,
    annotation VARCHAR NOT NULL,
    last_edit_time TIMESTAMP NOT NULL
);

CREATE TABLE subscriptions(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    user_id BIGINT NOT NULL
);

INSERT INTO places(place_name) VALUES('Северный');
INSERT INTO places(place_name) VALUES('Ольгино');
INSERT INTO places(place_name) VALUES('Килбокс');
INSERT INTO places(place_name) VALUES('Рикошет');
INSERT INTO places(place_name) VALUES('Убежище печатника');

INSERT INTO groups(group_name) VALUES('Песец');
INSERT INTO groups(group_name) VALUES('ОСК');
INSERT INTO groups(group_name) VALUES('Дикие');
INSERT INTO groups(group_name) VALUES('SURV');
INSERT INTO groups(group_name) VALUES('ЛСО');
INSERT INTO groups(group_name) VALUES('Red Fox');
INSERT INTO groups(group_name) VALUES('Голос Зоны');
INSERT INTO groups(group_name) VALUES('ВАСК');
INSERT INTO groups(group_name) VALUES('DOG''S BAND');

INSERT INTO genres(genre_name) VALUES('Воскреска');
INSERT INTO genres(genre_name) VALUES('Сценарная игра');
INSERT INTO genres(genre_name) VALUES('Большая игра');
INSERT INTO genres(genre_name) VALUES('Милсим');
INSERT INTO genres(genre_name) VALUES('Ролевая игра');
INSERT INTO genres(genre_name) VALUES('Соревнования');
INSERT INTO genres(genre_name) VALUES('Событие (конференция, выставка)');
INSERT INTO genres(genre_name) VALUES('Рейдовая');
INSERT INTO genres(genre_name) VALUES('Ночная');
INSERT INTO genres(genre_name) VALUES('Суточная');

INSERT INTO users(id, is_admin, is_true_admin) VALUES(434294239, 'TRUE', 'TRUE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(1733814577, 'TRUE', 'TRUE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(395233149, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(415882547, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(446274673, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(1945011574, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(1415439538, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(299076721, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(5422338715, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(5026935623, 'TRUE', 'FALSE');
INSERT INTO users(id, is_admin, is_true_admin) VALUES(439436332, 'TRUE', 'FALSE');
