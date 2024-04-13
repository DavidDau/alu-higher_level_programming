#!/usr/bin/python3
"""all cities by state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    # Execute an SQL query to retrieve city names based on the state name
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))

    # Fetch all the results from the executed query
    my_list = cursor.fetchall()

    # Print the city names separated by commas
    print(", ".join(city[0] for city in my_list))

    # Close the cursor and database connection
    cursor.close()
    db.close()
