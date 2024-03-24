#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
all cities of that state."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "WHERE states.name = %s "
        "ORDER BY cities.id")
    cur.execute(query, (argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
