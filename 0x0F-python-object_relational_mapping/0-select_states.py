#!/usr/bin/python3

import MySQLdb

connect = MySQLdb.connect(host="localhost", port=3306, user="root",
                          passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cursor = connect.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connect.close()
