#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

if __name__ == "__main__":
    myConn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    myCursor = myConn.cursor()
    myCursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for i in myCursor.fetchall():
        print(i)
