import sqlite3

#path = "/Documents/GitHub/SqlitePythonPractice/pythonsimplified/gta.db"
connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("create table gta (release integer, title text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

cursor.executemany("insert into gta values (?,?,?)", release_list)

#print database
for row in cursor.execute("select * from gta"):
    print(row)

#printing specific rows
print("***********************************************")
cursor.execute("select * from gta where  city=:c", {"c": "Liberty City"})
gta_search =  cursor.fetchall() 
print(gta_search )

cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?, ?)", ("Liberty City", "New York"))
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search )

# Now to manipulate the data
print("***********************************************")
for i in gta_search:
    changed = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(changed)

connection.close()