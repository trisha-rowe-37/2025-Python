#Imports pickle module to import and export data from trPlanetaryWeights.db
import pickle

def main():

    #Creates dictionary for conversion values and the planets as the keys
    dictPlanetConversions = {'Mercury':0.38, 'Venus':0.91, 'Moon':0.165, 'Mars':0.38,
                             'Jupiter':2.34, 'Saturn':0.93, 'Uranus':0.92,
                             'Neptune':1.12, 'Pluto':0.066}

    #Try except block for the initial opening of the file, + creating a dictionary to load info from file using pickle.load
    try:
        inputFile = open('trPlanetaryWeights.db', 'rb')
        pickledHistory = {}
        pickledHistory = pickle.load(inputFile)
        inputFile.close()

    #Used for if the file is empty/it doesnt exist.
    except Exception as err:
        print(f'General error: {format(err)}')
        pickledHistory = {}

    #Creates central dictionary for later use and adds file history to it so the info is not lost later when its overwritten using 'wb'
    dictPlanetHistory = {}

    #If pickled history exists then update the central dictionary
    if not pickledHistory:
        pass
    else:
        dictPlanetHistory.update(pickledHistory)

    #Central loop
    while True:
            #If user enters nothing, program closes.
            sName = str(input(f'What is your name (enter key to quit): '))
            if sName == '':
                exit()

            #Makes sName all uppercase letters to match the all uppercase keys for the history of the sName's.
            #If user enters previously entered name, they have the choice of viewing the history or not.
            if sName.upper() in dictPlanetHistory:
                print(f'{sName} is already in the history file. Enter a unique name.')
                while True:
                    sHistoryPrompt = input(f'Would you like to see the history? Y or N: ')
                    if sHistoryPrompt.upper() == 'Y':
                        print(f"\n{sName}, here are your weights on our Solar System's planets.\n")
                        historyOutput('Mercury',dictPlanetHistory[sName.upper()]['Mercury'])
                        historyOutput('Venus',dictPlanetHistory[sName.upper()]['Venus'])
                        historyOutput('the Moon',dictPlanetHistory[sName.upper()]['Moon'])
                        historyOutput('Mars',dictPlanetHistory[sName.upper()]['Mars'])
                        historyOutput('Jupiter',dictPlanetHistory[sName.upper()]['Jupiter'])
                        historyOutput('Saturn',dictPlanetHistory[sName.upper()]['Saturn'])
                        historyOutput('Uranus',dictPlanetHistory[sName.upper()]['Uranus'])
                        historyOutput('Neptune',dictPlanetHistory[sName.upper()]['Neptune'])
                        historyOutput('Pluto',dictPlanetHistory[sName.upper()]['Pluto'])
                        print('\n')
                        break
                    
                    elif sHistoryPrompt.upper() == 'N':
                        break
                    else:
                        print(f"You must enter 'Y' or 'N'.")
                        continue
                continue
                    
                                                                
            #Uses function that accounts for input data validation
            fWeight = floatInput('What is your weight: ')
            print(f"\n{sName}, here are your weights on our Solar System's planets.\n")

            #Creates central sub dictionary that will be used under dictPlanetHistory -- > sName -- > dictPersonWeights
            dictPersonWeights = {}

            #Using calculations function, prints and calculates each planetary weight for a new entry.
            #Also adds the return value from the function to the dictPersonWeights dictionary
            #Repeat this for all 10 calculations
            fMercury = calculations(dictPlanetConversions['Mercury'], fWeight, 'Mercury')
            dictPersonWeights['Mercury'] = fMercury
            
            fVenus = calculations(dictPlanetConversions['Venus'], fWeight, 'Venus')
            dictPersonWeights['Venus'] = fVenus
            
            fMoon = calculations(dictPlanetConversions['Moon'], fWeight, 'the Moon')
            dictPersonWeights['Moon'] = fMoon
            
            fMars = calculations(dictPlanetConversions['Mars'], fWeight, 'Mars')
            dictPersonWeights['Mars'] = fMars
            
            fJupiter = calculations(dictPlanetConversions['Jupiter'], fWeight, 'Jupiter')
            dictPersonWeights['Jupiter'] = fJupiter
            
            fSaturn = calculations(dictPlanetConversions['Saturn'], fWeight, 'Saturn')
            dictPersonWeights['Saturn'] = fSaturn
            
            fUranus = calculations(dictPlanetConversions['Uranus'], fWeight, 'Uranus')
            dictPersonWeights['Uranus'] = fUranus
            
            fNeptune = calculations(dictPlanetConversions['Neptune'], fWeight, 'Neptune')
            dictPersonWeights['Neptune'] = fNeptune
            
            fPluto = calculations(dictPlanetConversions['Pluto'], fWeight, 'Pluto')
            dictPersonWeights['Pluto'] = fPluto
            print('\n')
            
            #Adds the Name as a key and the prior dictionary as its value. Appends it to list from earlier that contains the history. 
            dictPlanetHistory.update({sName.upper():dictPersonWeights}) 

            #Opens the file once more for writing purposes, and pickle dumps all data into it, and closes.
            outputFile = open('trPlanetaryWeights.db','wb') 
            pickle.dump(dictPlanetHistory, outputFile)
            outputFile.close()
    
            
#Generic data validation function; positive, numeric, non-zero numbers
def floatInput(prompt):
    while True:
        try:
            result = float(input(prompt))
            if result > 0:
                return result
                break
        except ValueError:
            print(f'Number must be positive and above zero.')
            continue

#Function that calculates weight on each planet and prints using f string and proper formatting
def calculations(key, weight, planet):
    result = key * weight
    text = 'Weight on ' + planet + ':'
    print(f'{text:<20}{result:>15,.2f}')
    return result
    
#Similar function as above except its used if a user chooses yes to see history for that name. 
def historyOutput(planet, result):
    text = 'Weight on ' + planet + ':'
    print(f'{text:<20}{result:>15,.2f}')



main()
