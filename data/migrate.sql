\c cross_shooting;
DROP TABLE places;
DROP TABLE groups;
DROP TABLE genres;
DROP TABLE users;
DROP TABLE matches;
DROP TABLE user_bot_states;

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
    start_time TIMESTAMP NOT NULL,
    duration TIMESTAMP,
    place_id BIGINT NOT NULL,
    group_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    is_loneliness_friendly BOOLEAN NOT NULL
);

INSERT INTO places(place_name) VALUES('Totskiy Polygon');
INSERT INTO places(place_name) VALUES('Opushka');
INSERT INTO places(place_name) VALUES('Kolpino');
INSERT INTO places(place_name) VALUES('Sanctum Peterium Hive');

INSERT INTO groups(group_name) VALUES('Death Wolves');
INSERT INTO groups(group_name) VALUES('Punkihoy');
INSERT INTO groups(group_name) VALUES('Shoota Boyz');
INSERT INTO groups(group_name) VALUES('Suicide Squad');

INSERT INTO genres(genre_name) VALUES('Battle-Royal');
INSERT INTO genres(genre_name) VALUES('King of the Mount');
INSERT INTO genres(genre_name) VALUES('All Against All');

INSERT INTO users(id, is_admin, is_true_admin) VALUES('434294239', 'True', 'True')
