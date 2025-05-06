#Imports the Numerology class for general use
from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():

    #Recieves user input to enter into the class as parameters 
    while True:
        name = input(f'Enter a name: ')
        if len(name.strip()) == 0:
            print(f'Name cannot be empty. Try again: ')
            continue
        else:
            break
        
    while True:
        dob = input(f'Enter a date of birth (MM/DD/YYYY): ')
        if len(dob) == 10:
            if (dob[0:2].isnumeric() == True) and (dob[3:5].isnumeric() == True) and (dob[6:].isnumeric() == True):
                if (dob[2] == '/' or dob[2] == '-') and (dob[5] == '/' or dob[5] == '-'):
                    break
                else:
                    print(f'Date must be separated by either slashes or dashes.')
                    continue
                
            else:
                print(f'Date must contain only numbers.')
                continue
        else:
            print(f'Date must be in MM/DD/YYYY format.')
            continue

    #Creates a variable that uses the class and the user inputted data
    numerology = NumerologyLifePathDetails(name, dob)

    #Prints all data to the screen using the __str__ method defined in the numerology class
    print(numerology)

main()
