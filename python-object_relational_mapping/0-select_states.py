#!/usr/bin/python3 
"""Get em all"""
import sys
import MySQLdb
"""Module"""


def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = connection.cursor()

        # Execute query to fetch states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
