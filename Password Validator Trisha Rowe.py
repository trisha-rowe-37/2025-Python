def main():

    #Receive input for full name
    sName = input('Enter full name such as John Smith: ')
    
    #Converting full name into initials using split function and double indexes. 
    sNameSplit = sName.split()
    sInitialsPlaceholder = sNameSplit[0][0] + sNameSplit[1][0]
    sInitials = sInitialsPlaceholder.upper()
    
    

    #Creating loop for general use of password verification. 
    while True:
        sPassword = str(input(f'Enter new password: '))
        
        #Initializes fail-check accumulator that is used at end of code to check if user encountered error. 
        fails = 0

        #Creates new variable only checking the first four characters for the "pass check".
        sPass = sPassword[0:4]

        #Empty line for organization/neatness
        print(f'\n')

        #Creates all uppercase version of the password for the initial check later.
        initialCheck = sPassword.upper()

        #Checks length of password; has to be between 8 and 12 letters
        if len(sPassword) < 8 or len(sPassword) > 12:
            print(f'Password must be between 8 and 12 characters.')
            fails += 1

        #Fail if password contains any capitalization of "pass" 
        if sPass.upper() == "PASS":
            print(f'Password cannot start with "pass".')
            fails += 1

        #Fail if password does not contain an uppercase letter, vice versa for next if statement.
        if sPassword.islower() == True:
            print(f'Password must contain at least 1 uppercase letter.')
            fails += 1

        if sPassword.isupper() == True:
            print(f'Password must contain at least 1 lowercase letter.')
            fails += 1

        #Using the find function to determine if there are numbers present in this password. -1 returns when no number is present.
        #Back slashes used for neatness
        if sPassword.find("0") == -1 and \
             sPassword.find("1") == -1 and \
             sPassword.find("2") == -1 and \
             sPassword.find("3") == -1 and \
             sPassword.find("4") == -1 and \
             sPassword.find("5") == -1 and \
             sPassword.find("6") == -1 and \
             sPassword.find("7") == -1 and \
             sPassword.find("8") == -1 and \
             sPassword.find("9") == -1:
            print(f'Password must contain at least 1 number.')
            fails += 1

        #Similar to above if-statement. Determining use of special characters.
        if sPassword.find("!") == -1 and \
             sPassword.find("$") == -1 and \
             sPassword.find("@") == -1 and \
             sPassword.find("#") == -1 and \
             sPassword.find("^") == -1 and \
             sPassword.find("%") == -1:
            print(f'Password must contain at least 1 of these special characters: ! @ # $ % ^')
            fails += 1

        #Using initialCheck variable from top of while loop to determine whether the initials from full name input are present. 
        if initialCheck.find(sInitials) > -1:
            print(f'Password must not contain user initials.')
            fails += 1


        #Places all characters into list for duplicate check (lines 79-115)
        passwordList = []
        for char in sPassword.upper():
            passwordList.append(char)
        

        #Sorts the list alphanumerically
        sortedList = sorted(passwordList)
        

        #Removes all non duplicates and creates a list with one of each duplicate
        passLength = len(sPassword) -1
        index = 0
        index2 = 1
        dupeList = []
        for x in range(passLength):
            if sortedList[index] == sortedList[index2]:
                if sortedList[index] not in dupeList:
                    dupeList.append(sortedList[index])
            index += 1
            index2 += 1


        #Prints error message if dupes are present. Placing it above the for loop so it doesnt iterate multiple times. 
        if len(dupeList) >= 1:
            print(f'These characters appear more than once: ')
            fails += 1
        

        #Calls back to sorted list to use count method to see how many times it was used.
        # Uses a for loop to iterate for how many characters are in the dupeList
        lenDupe = len(dupeList)
        index = 0
        for x in range(lenDupe):
            dupeValue = dupeList[index]
            dupeCount = sortedList.count(dupeValue)
            print(f'{dupeValue}: {dupeCount} times')
            index += 1

        
        #Organizational Purpose line
        print(f'\n')   

        #If one fail is obtained from if statements, while loop restarts. If not, loop is broken, and password is good to use.         
        if fails == 0:
            print(f'Password is valid and OK to use.')
            break
        

 



main()
