#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    usrname_mysql = sys.argv[1]
    pass_mysql = sys.argv[2]
    database_name = sys.argv[3]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usrname_mysql,
        password=pass_mysql,
        database=database_name
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
        "ORDER BY states.id ASC"
    )

    for row in cursor:
        print(row)

    cursor.close()
    database.close()
