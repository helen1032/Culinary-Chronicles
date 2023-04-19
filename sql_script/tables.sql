-- breakfasts table:
CREATE TABLE IF NOT EXISTS breakfasts (
    id int NOT NULL,
    title varchar(800) NOT NULL,
    servings int NOT NULL,
    ingredients varchar(800) NOT NULL,
    directions varchar(1000) NOT NULL,
    PRIMARY KEY (id)
);
