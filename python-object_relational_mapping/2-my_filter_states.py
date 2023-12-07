#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    usrname_mysql = sys.argv[1]
    pass_mysql = sys.argv[2]
    database_name = sys.argv[3]
    state_name_search = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usrname_mysql,
        password=pass_mysql,
        database=database_name
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name ='{}'"
        "ORDER BY states.id ASC".format(state_name_search)
    )

    for row in cursor:
        print(row)

    cursor.close()
    database.close()
