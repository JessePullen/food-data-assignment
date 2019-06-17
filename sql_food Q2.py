import sqlite3
#Database connection
connection = sqlite3.connect("food.db")
cursor = connection.cursor()

prevViolations = []

#SQL query to find distinct businesses with at least one violation
cursor.execute("""SELECT DISTINCT v.serial_number, i.facility_name, i.facility_address, i.facility_zip, i.facility_city 
               FROM violations v, inspections i WHERE v.serial_number = i.serial_number ORDER BY i.facility_name ;""") 
#Call the query and append query data into list for implementation and print to console
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
prevViolations.append(result)
    
#Create prevViolations table
prevViolationsTable = """
CREATE TABLE IF NOT EXISTS previous_violations (
serial_number CHAR(9),
facility_name VARCHAR(30),
facility_address VARCHAR(30),
facility_zip CHAR(5),
facility_city VARCHAR(30) 
);"""
connection.execute(prevViolationsTable)

#Inserts queried data into new previous_violations table
for list in prevViolations:
    cursor.executemany("""INSERT INTO previous_violations (serial_number, facility_name, facility_address, facility_zip, facility_city) 
                        VALUES (?, ?, ?, ?, ?)""", prevViolations[0])
    
#SQL query for violations for each business counted and ordered
cursor.execute("""SELECT COUNT(v.serial_number), i.facility_name, i.facility_address, i.facility_zip, i.facility_city FROM violations v, inspections i 
               WHERE v.serial_number = i.serial_number GROUP BY i.facility_name ORDER BY COUNT(v.serial_number) DESC, i.facility_name ;""") 
#Call the query and print to console
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)

#Commit and close database
connection.commit()
connection.close() 