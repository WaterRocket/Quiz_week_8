import matplotlib.pyplot as plt
import sqlite3
#Declare variables to store lists
years = []
co2 = []
temp = []

connection = sqlite3.connect(r"climate.db")
cursor = connection.cursor()

cursor.execute("SELECT*FROM ClimateData")
result = cursor.fetchall()

#Iterate through rows and append to lists
for r in result:
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
