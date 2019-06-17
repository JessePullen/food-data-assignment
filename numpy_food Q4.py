import matplotlib.pyplot as plt
import sqlite3
#Database connection
connection = sqlite3.connect("food.db")
cursor = connection.cursor()

#containers for all california
date = []
violations = []
postCode = []

#containers for highest total
highestViolations = {}
hDate = []
hViolations = []
hPostCode = []

#containers for all McDonald's and Burger King fast food
ffDate = []
ffViolations = []
ffPostCode = []



#SQL query for all california
cursor.execute("""SELECT STRFTIME('%m-%Y', i.activity_date) AS 'month', COUNT(v.serial_number), i.facility_zip
               FROM violations v, inspections i WHERE v.serial_number = i.serial_number AND i.activity_date BETWEEN '2015-07-01' AND '2017-12-31'
               GROUP BY v.serial_number ORDER BY STRFTIME('%Y-%m', i.activity_date);""" )
#Call the query and append query data into lists for graphing
result = cursor.fetchall() 
for r1, r2, r3 in result:
    date.append(r1)
    violations.append(r2)
    postCode.append(r3)
    
#AVG violations per month for California combined
plt.title('AVG Violations Per Month for California')
plt.plot(date, violations, 'bo')
plt.xlabel('Date')
plt.ylabel('Violations')
plt.xticks(rotation=270)
plt.show()




#Finding total violations
#Count violations per post code
for r in result:
    violation = r[1]
    pCode = r[2]
    highestViolations[pCode] = highestViolations.get(pCode, 0) + violation

#Assign highest and lowest value's key in the dict as mostViolations for graphing
mostViolations = max(highestViolations, key=lambda key: highestViolations[key])
leastViolations = min(highestViolations, key=lambda key: highestViolations[key])


#SQL query implementing the dictionary value for the business with the highest and least violations
cursor.execute("""SELECT STRFTIME('%m-%Y', i.activity_date) AS 'month', COUNT(v.serial_number), i.facility_zip
               FROM violations v, inspections i WHERE v.serial_number = i.serial_number AND (i.facility_zip is ? OR i.facility_zip is ?)
               GROUP BY i.facility_zip ORDER BY STRFTIME('%Y-%m', i.activity_date);""",(mostViolations, leastViolations,)) 
#Call the query and append query data into lists for graphing
hResult = cursor.fetchall() 
for r1, r2, r3 in hResult:
    hDate.append(r1)
    hViolations.append(r2)
    hPostCode.append(r3)


#AVG violations per month for the postcode with the highest total violations
plt.figure()
plt.title('AVG Violations Per Month for the Business With the Highest and Lowest Violations')
plt.plot(hDate, hViolations, 'go')
plt.xlabel('Date')
plt.ylabel('Violations')
plt.show()




#count serial in day / number of serial in month
cursor.execute("""SELECT STRFTIME('%m-%Y', i.activity_date) AS 'month', COUNT(v.serial_number), i.facility_zip
               FROM violations v, inspections i WHERE v.serial_number = i.serial_number 
               AND (i.facility_name LIKE "%MCDONALD%" OR i.facility_name LIKE "%KING%")
               GROUP BY v.serial_number ORDER BY STRFTIME('%Y-%m', i.activity_date);""" )
#Call the query and append query data into lists for graphing
ffResult = cursor.fetchall() 
for r1, r2, r3 in ffResult:
    ffDate.append(r1)
    ffViolations.append(r2)
    ffPostCode.append(r3)

#AVG violations per month for Burger King and Mcdonalds
plt.figure()
plt.title("AVG Violations Per Month for Burger King and McDonald's")
plt.plot(ffDate, ffViolations, 'ro')
plt.xlabel('Date')
plt.ylabel('Violations')
plt.xticks(rotation=270)
plt.show()


#Commit and close database
connection.commit()
connection.close() 