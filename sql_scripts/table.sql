-- breakfast table:
CREATE TABLE IF NOT EXISTS breakfast (
    id int NOT NULL AUTO_INCREMENT,
    name varchar() NOT NULL,
    ingredients varchar() NOT NULL,
    methods varchar() NOT NULL,
    PRIMARY KEY (id)
);

-- lunch table:
CREATE TABLE IF NOT EXISTS lunch (
    id int NOT NULL AUTO_INCREMENT,
    name varchar() NOT NULL,
    ingredients varchar() NOT NULL,
    methods varchar() NOT NULL,
    PRIMARY KEY (id)
);

-- dinner table:
CREATE TABLE IF NOT EXISTS dinner (
    id int NOT NULL AUTO_INCREMENT,
    name varchar() NOT NULL,
    ingredients varchar() NOT NULL,
    methods varchar() NOT NULL,
    PRIMARY KEY (id)
);

-- dessert table:
CREATE TABLE IF NOT EXISTS dessert (
    id int NOT NULL AUTO_INCREMENT,
    name varchar() NOT NULL,
    ingredients varchar() NOT NULL,
    methods varchar() NOT NULL,
    PRIMARY KEY (id)
);