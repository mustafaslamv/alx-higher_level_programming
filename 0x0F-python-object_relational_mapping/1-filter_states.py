#!/usr/bin/python3
"""script that lists all states with a name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    myConn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    myCursor = myConn.cursor()
    myCursor.execute("SELECT * FROM states\
                     WHERE BINARY name LIKE 'N%' ORDER BY states.id ASC")
    for i in myCursor.fetchall():
        print(i)
    myCursor.close()
    myConn.close()
