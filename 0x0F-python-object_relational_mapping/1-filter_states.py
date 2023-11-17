#!/usr/bin/python3
"""defines a script that lists all states with a name starting
with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                               passwd="root", db="hbtn_0e_0_usa",
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY states.id""")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
