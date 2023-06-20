#Script to show the data in the Terminal
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")

sql_stmt = f"SELECT * FROM drivers"

cur.execute(sql_stmt)
response = cur.fetchall()

for row in response:
    print(row[0], row[1], row[2], row[3])

cur.close()
mydb.close()