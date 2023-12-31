#!/usr/bin/python3
"""script displays all values in the states where name matches the argument
    but It's safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    stateName = sys.argv[4]

    myConn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    myCursor = myConn.cursor()
    query = "SELECT * FROM states\
             WHERE BINARY name = %s\
             ORDER BY states.id ASC"
    myCursor.execute(query, (stateName,))
    for i in myCursor.fetchall():
        print(i)
    myCursor.close()
    myConn.close()
