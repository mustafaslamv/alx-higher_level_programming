#!/usr/bin/python3
""" script that takes in the name of a state as an argument
    and lists all cities of that state using the db hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    myConn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    myCursor = myConn.cursor()
    query = """
        SELECT name FROM cities
        WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)
        ORDER BY cities.id ASC
    """
    myCursor.execute(query, (state_name,))
    result = myCursor.fetchall()
    if result:
        for i, city in enumerate(result):
            if (i < len(result) - 1):
                print(city[0], end=", ")
            else:
                print(city[0])
    myCursor.close()
    myConn.close()
