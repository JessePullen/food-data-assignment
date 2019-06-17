Each program should be ran in the following order as they each create files that are used by the next program.
Running the programs consecutively require the created files to be deleted.
Each program can also take minutes to run due to the large amount of data being used. Finished is printed when the program is finished running.
These programs were ran in Spyder to show the graphs in console.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 1 – Access the workbooks and create a database 
Create a Python script (db_create.py) to perform the following tasks: 
-Open the excel files.
-Create a SQLite database with two tables, one for each excel file. Each column in the excel files should correspond to a column in the tables. 
-Import the data from the excel files to the corresponding tables in the database.

db_create.py  Q1
Run the program and a database is created called food.db. A new database will not be created if the program is re-run.
The program reads the spreadsheet data, creates tables with column names from the spreadsheets and inserts the data into the tables.
The insert uses ? placeholders and assigns each element return from the query to a variable name to replace a ? that is found in the valuesV or valuesI list.
Create table if not exists was used to not re-create tables that are already in the database.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 2 – Query the database 
Create a Python script (sql_food.py) to perform the following tasks: 
-List the distinctive businesses that have had at least 1 violation ordered alphabetically to the console and then write their name, address, zip code and city into a new database table called “Previous Violations”.
-Print a count of the violations for each business that has at least 1 violation to the console along with their name ordered by the number of violations.

sql_food.py  Q2
This program queries the existing database with a joined query for the relevant information.
A new table is created to store this information. The program uses the same method of inserting the data using the ? placeholder.
The second query is to count the businesses with at least one violation using group by.
This program also prints the query results to the console.
The program does not recreate the food.db file.
Create table if not exists was used to not re-create tables that are already in the database.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 3 – Excel via Python 
Create a Python script (excel_food.py) to perform the following tasks: 
-Create a new workbook named “ViolationTypes.xlsx”. 
-Create a sheet named “Violations Types”. 
-Query the database and calculate the number of each type of violation based on violation code. 
-Write the relevant data into the worksheet you created. This should show the total number of violations, then list how that is broken down by violation code, including the description of the violation code

excel_food.py  Q3
This program creates a new spreadsheet and worksheet named Violation Types.
The A1, B1 and C1 columns are given values for the headers of the information.
There is a query using count to count the number of serial numbers(violations) grouped by the code to tally the number of codes that are present.
The query values are directly appended to the spreadsheet.
wb.save is used to save and/or create the spreadsheet. From my testing this did not recreate or interfere with the current spreadsheet
and the program can be re-run without consequences that I could see.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 4 – Numpy in Python 
Create a Python script (numpy_food.py) to perform the following tasks: 
-Query the database and retrieve data to calculate the average violations for every month between July 2015 and December 2017 for each postcode.   
-Use MatPlotLib to plot the follow data over time: 
	-The violations per month for the postcode(s) with the highest total violations 
	-The violations per month for the postcode(s) with the greatest variance (difference) between the lowest and highest number of violations for all months. 
	-The average violations per month for ALL of California (all postcodes combined) 
	-The violations per month for all McDonalds and Burger Kings. This will require a new query as it is not grouped by postal code. 

numpy_food.py  Q4
This program uses matplotlib to graph the data of the queries.
There is a number of list containers and one dictionary used for the different queries.
The first query changes the date format that was being used in my table and groups the data in months instead of days.
The query data is appended into 3 lists using indexing to select the appropriate output to the appropriate list.
The data is then plotted directly.

The second query uses a dictionary to store the postcode with the counted number of serials to find the lowest and highest post code.
The dict is min and maxed for the highest value and is then used in the query using a ? placeholder.
The data is then appended into appropriate lists as above and graphed.

The third query uses LIKE to find the Mcdonalds' and Burger King's as they have numbers in the spreadsheet after the name so IN cannot be used effectively.
The data is again appended to lists and plotted.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------