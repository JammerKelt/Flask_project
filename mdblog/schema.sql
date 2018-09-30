DROP table if EXISTS articles;
CREATE TABLE articles (
    id INTEGER PRIMARY KEY autoincrement,
    title text NOT NULL,
    content text NOT null
);