CREATE DATABASE pet_hotel


CREATE TABLE owner (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
);

CREATE TABLE pet (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    breed VARCHAR(80),
    color VARCHAR(80),
    checked_in VARCHAR(80),
    owner_id integer REFERENCES owner
);
