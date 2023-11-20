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
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    myCursor.execute(query, (state_name,))
    result = myCursor.fetchall()
    formatted_result = ', '.join(item[0] for item in result)
    print(formatted_result)

    myCursor.close()
    myConn.close()
