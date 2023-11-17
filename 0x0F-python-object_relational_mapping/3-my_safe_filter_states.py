#!/usr/bin/python3
"""defines a script that takes an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
safe from sql injections"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (query, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
