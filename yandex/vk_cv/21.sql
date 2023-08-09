""" two tables 
users: id, name, surname, salary, birth_date
books: id, header, author_id, year, text

print ids, names and surnames of users with header and year of publishing 
authors without books and books without authours dont return
"""

SELECT users.id, users.name, users.surname, books.header, books.year
FROM users
INNER JOIN books
ON users.id = books.author_id

"""number of rows in a table with cross join 7 rows and 3 rows will be 

7*3 = 21 rows

"""
"""to get current date in DD format use SELECT CURRENT_DATE()"""
""" all datatypes in SQL are text, numbers, dates, boolean, binary data"""

CREATE TABLE sql_test_a 
( 
    ID         VARCHAR2(4000 BYTE), 
); 

CREATE TABLE sql_test_b 
( 
    ID         VARCHAR2(4000 BYTE) 
); 


INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('1');

INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('2');

INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('3');

INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('4');

INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('5');

INSERT INTO sql_test_a (ID, FIRST_NAME, LAST_NAME) VALUES ('6');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('NULL');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('0');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('1');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('1');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('1');

INSERT INTO sql_test_b (ID, FIRST_NAME, LAST_NAME) VALUES ('1');

SELECT * FROM sql_test_b INNER JOIN sql_test_a ON sql_test_a.ID=sql_test_b.ID;

CREATE TABLE sql_test_a ( 
ID INT(6) UNSIGNED 
); 

CREATE TABLE sql_test_b ( 
ID VARCHAR(6)
); 


INSERT INTO sql_test_a (ID) VALUES ('1');

INSERT INTO sql_test_a (ID) VALUES ('2');

INSERT INTO sql_test_a (ID) VALUES ('3');

INSERT INTO sql_test_a (ID) VALUES ('4');

INSERT INTO sql_test_a (ID) VALUES ('5');

INSERT INTO sql_test_a (ID) VALUES ('6');

INSERT INTO sql_test_b (ID) VALUES ('NULL');

INSERT INTO sql_test_b (ID) VALUES ('0');

INSERT INTO sql_test_b (ID) VALUES ('1');

INSERT INTO sql_test_b (ID) VALUES ('1');

INSERT INTO sql_test_b (ID) VALUES ('1');

INSERT INTO sql_test_b (ID) VALUES ('1');