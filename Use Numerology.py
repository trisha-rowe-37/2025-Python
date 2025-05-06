#Imports the Numerology class for general use
from Numerology import Numerology

def main():

    #Recieves user input to enter into the class as parameters
    name = input(f'Enter a name: ')
    dob = input(f'Enter a date of birth (MM/DD/YYYY): ')

    #Creates a variable that uses the class and the user inputted data
    numerology = Numerology(name, dob)

    #Prints all data to the screen using the __str__ method defined in the numerology class
    print(numerology.__str__())

main()
