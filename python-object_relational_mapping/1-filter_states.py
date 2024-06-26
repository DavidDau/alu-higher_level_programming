#!/usr/bin/python3
"""
All states with a name starting with N (upper N)
from the database  hbtn_0e_0_us:
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    my_list = cursor.fetchall()
    for j in my_list:
        if j[1][0] == 'N':
            print(j)
    cursor.close()
    db.close()
