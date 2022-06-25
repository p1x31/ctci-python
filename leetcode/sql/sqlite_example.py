import sqlite3

# QUERY_CREATE = '''CREATE TABLE IF NOT EXISTS MeetUp(
#     id INT PRIMARY KEY,
#     City TEXT,
#     Date TEXT);'''

QUERY_CREATE = '''Create table If Not Exists Logs (
    id int, num int);'''

#QUERY_INSERT = 'INSERT INTO MeetUp VALUES(?, ?, ?);'
QUERY_INSERT = 'INSERT INTO Logs VALUES(?, ?);'
def make_db(db_name, data):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(QUERY_CREATE)
    cur.executemany(QUERY_INSERT, data)
    conn.commit()
    conn.close()

# data = [
# (1, 'Amsterdam', '2022-01-01'),
# (2, 'Moscow', '2022-01-02'),
# (3, 'Berlin', '2022-01-04'),
# (4, 'New York', '2022-01-07'),
# (5, 'Berlin', '2022-01-08'),
# (6, 'Paris', '2022-01-08'),
# (7, 'Paris', '2022-01-10'),
# (8, 'Tokyo', '2022-01-13'),
# (9, 'Beijing', '2022-01-15'),
# (10, 'Melbourne', '2022-01-18'),]

data = [(1, '1'),
        (2, '1'),
        (3, '1'),
        (4, '2'),
        (5, '1'),
        (6, '2'),
        (7, '2'),]
make_db('DataBase.db', data)