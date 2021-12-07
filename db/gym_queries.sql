DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS memberships;

CREATE TABLE memberships(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    cost INT,
    free_classes INT
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    -- membership VARCHAR(255),
    membership_id INT REFERENCES memberships(id) ON DELETE CASCADE,
    classes_remaining INT,
    wallet INT
);

CREATE TABLE gym_classes(
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    duration INT,
    available_slots INT,
    type VARCHAR(255),
    entry_fee INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_classes_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);