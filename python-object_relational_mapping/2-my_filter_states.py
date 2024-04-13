#!/usr/bin/python3
"""filter states by user input"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    # Execute an SQL query to retrieve data from the 'states' table
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
            id ASC".format(argv[4]))

    # Fetch all the results from the executed query
    my_list = cursor.fetchall()

    # Iterate through the results and print matching rows
    for j in my_list:
        if j[1] == argv[4]:
            print(j)

    # Close the cursor and database connection
    cursor.close()
    db.close()
