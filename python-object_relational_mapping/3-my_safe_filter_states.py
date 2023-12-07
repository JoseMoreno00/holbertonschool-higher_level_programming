#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
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
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER\
        BY states.id ASC",
        (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
