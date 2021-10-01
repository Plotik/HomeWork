PRAGMA FOREIGN_KEY = ON;

DROP TABLE tag;
CREATE TABLE tag(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label VARCHAR(255)
);

DROP TABLE category;
CREATE TABLE category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_name VARCHAR(255)
);

DROP TABLE author;
CREATE TABLE author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    a_name VARCHAR(255)
);

DROP TABLE book;
CREATE TABLE book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER,
    name VARCHAR(255) NOT NULL,
    years VARCHAR(4) NOT NULL,
    release VARCHAR(255) NOT NULL,
    pages VARCHAR(4) NOT NULL,
    category_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

INSERT INTO
    tag (label)
    values ('RU'), ('EN'), ('TOP5'), ('TOP10'), ('TOP50'), ('TOP100');

INSERT INTO
    category (cat_name)
    values ('Modern'), ('Nature'), ('Protest'), ('Popular Culture');

INSERT INTO
    author (a_name)
    values ('Anton Chekhov'), ('Vladimir Nabokov'), ('Franz Kafka'), ('Albert Einstein'), ('Edward O. Wilson'), ('Lillian Smith'),
           ('Paul Goodman'), ('Rudyard Kipling'), ('Albert Camus'), ('Henry James'), ('Raymond Chandler'), ('Stephen King');

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (1, 'The Three Sisters', '1901', '01.10.2021', '444', 1, 5);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (2, 'The Three Sisters', '1901', '01.10.2021', '444', 3, 3);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (2, 'Lolita', '1955', '12.01.2021', '222', 4, 5);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (3, 'Lolita', '1955', '12.01.2021', '222', 2, 6);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (3, 'The Metamorphosis', '1915', '15.03.2021', '333', 1, 2);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (3, 'The Metamorphosis', '1915', '15.03.2021', '333', 2, 4);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (4, 'The Meaning of Relativity', '1922', '06.07.2021', '233', 2, 2);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (5, 'The Diversity of Life', '1992', '01.02.2021', '50', 3, 2);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (6, 'Strange Fruit', '1944', '17.06.2021', '140', 3, 3);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (7, 'Growing Up Absurd', '1960', '13.04.2021', '350', 3, 2);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (8, 'Kim', '1901', '08.03.2021', '366', 3, 2);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (8, 'Kim', '1901', '08.03.2021', '366', 3, 4);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (9, 'The Stranger', '1942', '25.09.2021', '234', 4, 3);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (10, 'The Turn of the Screw', '1898', '28.04.2021', '656', 4, 2);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (10, 'The Turn of the Screw', '1898', '28.04.2021', '656', 3, 4);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (11, 'The Big Sleep', '1939', '05.05.2021', '300', 4, 1);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (11, 'The Big Sleep', '1939', '05.05.2021', '300', 4, 5);

INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (11, 'Carrie', '1974', '19.01.2021', '246', 4, 3);
INSERT INTO
    book (author_id, name, years, release, pages, category_id, tag_id)
    values (12, 'Carrie', '1974', '19.01.2021', '246', 4, 4);

.headers on
.mode column
.width  20 25 4 10 5 20 10

--SELECT a_name as Author, name as Book_Name, years as Years, release as Release,
--    pages as Pages, cat_name as Category, label as Tag FROM book
--    JOIN author ON author_id = author.id
--    JOIN category ON category_id = category.id
--    JOIN tag ON tag_id = tag.id;

SELECT cat_name as Category, COUNT(name) as Book_Name FROM book
    JOIN category ON category_id = category.id
    GROUP BY category_id;

SELECT cat_name as Category, AVG(pages) as Avr_Pages FROM book
    JOIN category ON category_id = category.id
    GROUP BY category_id;

SELECT cat_name as Category, MAX(pages) as Max_Pages FROM book
    JOIN category ON category_id = category.id
    GROUP BY category_id;

SELECT cat_name as Category, MIN(pages) as Min_Pages FROM book
    JOIN category ON category_id = category.id
    GROUP BY category_id;

SELECT release as Release_Date, COUNT(name) as Book_Name FROM book
    GROUP BY release;

SELECT a_name as Author, COUNT(name) as Book_Name FROM book
    JOIN author ON author_id = author.id
    GROUP BY author_id;