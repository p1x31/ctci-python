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