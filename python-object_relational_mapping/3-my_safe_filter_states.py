#!/usr/bin/python3
"""sql injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    # Execute an SQL query to retrieve data from the 'states' table
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))

    # Fetch all the results from the executed query
    my_list = cursor.fetchall()

    # Iterate through the results and print each row
    for j in my_list:
        print(j)

    # Close the cursor and database connection
    cursor.close()
    db.close()
