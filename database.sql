CREATE DATABASE pet_hotel


CREATE TABLE owner (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60)
);

CREATE TABLE pet (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    breed VARCHAR(80),
    color VARCHAR(80),
    checked_in BOOLEAN DEFAULT false,
    owner_id integer REFERENCES owner
);

INSERT INTO "owner"
    ("name")
VALUES
    ('Frank'),
    ('Marge');

INSERT INTO "pet"
    ("name", "breed", "color", "checked_in", "owner_id")
VALUES
    ('Fido', 'mutt', 'brown', 'false', '1'),
    ('Mittens', 'alley', 'black', 'false', '2');