CREATE TABLE IF NOT EXISTS products(
    id INTEGER primary key autoincrement,
    name varchar(50) not null,
    price FLOAT not null,
    describe TEXT
);

CREATE TABLE IF NOT EXISTS users(
    id INTEGER primary key autoincrement,
    name varchar(50) not null,
    surname varchar(50) not null,
    password varchar(20) not null,
    email varchar(50) not null,
    phone_number INTEGER not null
);