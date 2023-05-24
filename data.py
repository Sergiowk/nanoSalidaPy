import ergast_py
import datetime

"""
e = ergast_py.Ergast()
race_results = e.season(2023).round(5).get_results()

print(race_results)
"""
e = ergast_py.Ergast()
drivers = e.season(datetime.date.today().year).get_drivers()

for driver in drivers:
    print("Driver ID:", driver.driver_id)
    print("Permanent Number:", driver.permanent_number)
    print("Code:", driver.code)
    print("URL:", driver.url)
    print("Given Name:", driver.given_name)
    print("Family Name:", driver.family_name)
    print("Date of Birth:", driver.date_of_birth)
    print("Nationality:", driver.nationality)
    #[name] = driver.given_name
    #print (name)

#print(name)

#print(drivers)

