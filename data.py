import ergast_py

e = ergast_py.Ergast()
race_results = e.season(2023).round(5).get_results()

print(race_results)
