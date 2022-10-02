-- Active: 1664620083806@@127.0.0.1@3306@test
CREATE TABLE test(

    id int PRIMARY KEY, 
    name VARCHAR(50)


);


INSERT INTO test
VALUES(1,'dheeraj');

ALTER TABLE test
ADD COLUMN age int;

UPDATE test
set age = 17
where id = 1;

SELECT *
from test;

SELECT *
from test;

INSERT INTO test
VALUES (5,'bota',20);



SELECT *
from test;