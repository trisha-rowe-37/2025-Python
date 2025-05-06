#Imports sqlite3 to use the database features
#Imports csv to read from comma separated values in the .txt files
import sqlite3
import csv

def main():

    #Creates or connects to the PythonSqlInteract.db file
    dBaseConnect = sqlite3.connect("PythonSqlInteract.db")

    #Assigns a variable to the cursor
    dBaseCursor = dBaseConnect.cursor()

    #Creates 3 different tables with some overlapping column names
    dBaseConnect.execute("CREATE TABLE IF NOT EXISTS Employee(EmployeeID int, Name text)")
    dBaseConnect.execute("CREATE TABLE IF NOT EXISTS Pay(EmployeeID int, Year int, Earnings real)")
    dBaseConnect.execute("CREATE TABLE IF NOT EXISTS SocialSecurityMinimum(Year int, Minimum real)")

    #Creates a half-finished string that is finished in the inserter function
    #Creates a Reset Variable for the function as well
    #Initializes a ThreeColumns variable and gives  it a true or false depending on if the txt file has 3 columns to add or 2
    #Uses this function 3 separate times for 3 different tables and files
    InsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
    EmployeeReset = InsertEmployee
    ThreeColumns = False
    inserter("Employee.txt", InsertEmployee, EmployeeReset, dBaseCursor, ThreeColumns)

    InsertPay = "INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES("
    PayReset = InsertPay
    ThreeColumns = True
    inserter("Pay.txt", InsertPay, PayReset, dBaseCursor, ThreeColumns)

    InsertSocial = "INSERT INTO SocialSecurityMinimum(Year, Minimum) VALUES("
    SocialReset = InsertSocial
    ThreeColumns = False
    inserter("SocialSecurityMinimum.txt", InsertSocial, SocialReset, dBaseCursor, ThreeColumns)

    #Saves changes to the database file
    dBaseConnect.commit()

    #Executes and selects specific columns FROM specific tables and joins some together
    dBaseCursor.execute(
        "SELECT Employee.Name, Pay.Year, Pay.Earnings, SocialSecurityMinimum.Minimum "
        "FROM Employee "
        "JOIN Pay ON Employee.EmployeeID = Pay.EmployeeID "
        "JOIN SocialSecurityMinimum ON Pay.Year = SocialSecurityMinimum.Year "
        )

    #Prints the column headers
    #Creates an empty list that is added to when the selected data is iterated over by a for loop
    #If there is a duplicate line, the loop skips to the next iteration, if its a new line, it is printed
    #Adds if statement to check if the earnings number is greater than the minimum, and prints yes or no depending on which one it is
    print(f'{"Employee Name":<20}Year{"Earnings":>15}      {"Minimum Include":>15}')
    selected = dBaseCursor.fetchall()
    isInList = []
    for x in selected:
        if x in isInList:
            continue
        isInList.append(x)
        
        name, year, earnings, minimum = x
        if earnings >= minimum:
            y = "Yes"
        else:
            y = "No"
        print(f'{name:<20}{year}{earnings:>15}{minimum:>15} {y}')
                        
#Creates inserter functiion which takes 5 arguments
#Opens the filename argmument  for reading, and uses the csv to read each line except the first one using next(reader)
#Uses if elif statement ot determine if TorF takes 2(false) or 3(true) columns
#Resets the table after each iteration
def inserter(filename, InsertTable, TableReset, cursor, TorF):
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
    
        next(reader)
    
        for row in reader:
            if TorF == False:
                InsertTable += (f"{row[0]}, '{row[1]}')")
                cursor.execute(InsertTable)
                InsertTable = TableReset
            elif TorF == True:
                InsertTable += (f"{row[0]}, '{row[1]}', '{row[2]}')")
                cursor.execute(InsertTable)
                InsertTable = TableReset



main()
