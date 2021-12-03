DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    wallet INT
);

CREATE TABLE gym_classes(
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    duration INT,
    available_slots INT,
    type VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_classes INT REFERENCES gym_classes(id) ON DELETE CASCADE
);