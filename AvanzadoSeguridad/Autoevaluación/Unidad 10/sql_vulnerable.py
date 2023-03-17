#!/usr/bin/python3

import sqlite3

connection = sqlite3.connect("database.sqlite")

cursor = connection.cursor()

identificador =1
valor='c'

cursor.execute("SELECT * FROM tabla WHERE id = '%s'" % identificador)
cursor.execute("INSERT INTO tabla VALUES ('a', 'b', '%s')" % valor)
cursor.execute("DELETE FROM tabla WHERE id = '%s'" % identificador)
cursor.execute("UPDATE tabla SET value = 'b' WHERE id = '%s'" % identificador)

connection.close()
