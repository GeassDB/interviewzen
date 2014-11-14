CREATE TABLE collection
(
    cid     int         NOT NULL    AUTO_INCREMENT,
    user    tinytext    NOT NULL,
    book    tinytext    NOT NULL,
    tag     tinytext    NULL,
    PRIMARY KEY (cid)
) ENGINE = Maria;

a)
SELECT DISTINCT book FROM collection WHERE user = <user>

b)
SELECT DISTINCT tag FROM collection WHERE user = <user>

c)
SELECT DISTINCT book FROM collection WHERE user = <user> AND tag = <tag>

d)
