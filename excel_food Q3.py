import openpyxl
import sqlite3
#Database connection
connection = sqlite3.connect("food.db")
cursor = connection.cursor()

li = []

#Create new workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Violation Types'

#Add names for columns
sheet['A1'] = 'Count'
sheet['B1'] = 'Code'
sheet['C1'] = 'Description'

#SQL query to find number of each violation based on violation code
cursor.execute("""SELECT COUNT(violation_code), violation_code, violation_description FROM violations 
               GROUP BY violation_code ORDER BY COUNT(violation_code) DESC, violation_code;""") 
result = cursor.fetchall() 

#Iterate through query results and append to spreadsheet
for i in result:
    sheet.append(i)

#Save contents of spreadsheet
wb.save('ViolationTypes.xlsx')

#Commit and close database
connection.commit()
connection.close() 