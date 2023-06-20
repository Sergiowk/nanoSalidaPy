#Batch process to get the data from the API
import mysql.connector
import ergast_py
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

cur = mydb.cursor()
cur.execute("USE DB")


e = ergast_py.Ergast()
#Get current drivers
drivers = e.season(datetime.date.today().year).get_drivers()

#Inserting the drivers into the DB
for driver in drivers:
    sql_stmt = f"INSERT INTO drivers(name, number, nationality, dob) VALUES('{driver.given_name} {driver.family_name}', '{driver.permanent_number}','{driver.nationality}', '{driver.date_of_birth}')"
    cur.execute(sql_stmt)
    mydb.commit()

cur.close()
mydb.close()