#imports collections module to use the default dictionary (i needed to have the values default to lists)
import collections


def main():
    #Opens the file for reading and places each line into a list as a string for each entry
    fileInput = open('RealEstateData.csv','r')
    mainList = fileInput.readlines()
    
    #Initializes list that separates each field from each other by removing the commas
    #Iterates over each entry in main list for this.
    #Adds splitlist as entries to a nested list.
    sepList = []
    for row in mainList:
    
        splitList = row.strip().split(",")
        sepList.append(splitList)

    #Creates dictionary that makes the 1 index of each of lists in the sepList into a key value, and the 8 index the value (the value being a list)
    #If the City (1 index) already exists isnide the dictionary, append to the end of the value list for prices. 
    #If the city does not exist already, initialize a key-value for the dictionary
    #Uses if elif to remove the first line from being added and changes the price values from string to float for later calculations.
    cityDict = collections.defaultdict(list)
    for x in sepList:
        if x[1] == 'city':
            pass
        elif x[1] != 'city':
            if x[1] in cityDict:
                cityDict[x[1]].append(float(x[8]))
            elif x[1] not in cityDict:
                cityDict[x[1]] = [float(x[8])]
    
    #Same process as above but with the property types instead
    propDict = collections.defaultdict(list)
    for x in sepList:
        if x[7] == 'type':
            pass
        elif x[7] != 'type':
            if x[7] in propDict:
                propDict[x[7]].append(float(x[8]))
            elif x[7] not in propDict:
                propDict[x[7]] = [float(x[8])]
    
    #Same process as above but with the zip codes instead
    zipDict = collections.defaultdict(list)
    for x in sepList:
        if x[2] == 'zip':
            pass
        elif x[2] != 'zip':
            if x[2] in zipDict:
                zipDict[x[2]].append(float(x[8]))
            elif x[2] not in zipDict:
                zipDict[x[2]] = [float(x[8])]
    
    #Creates a dictionary for the prices for output of min max avg median sum
    priceList = []
    for x in sepList:
        if x[8] == 'price':
            pass
        elif x[8] != 'price':
            priceList.append(float(x[8]))
    
    #Sorts price list to find median, min, max
    priceList.sort()
    
    #Determines average price
    priceLength = len(priceList)
    average = sum(priceList) / priceLength

    #Determines index of median
    median = priceLength /2
    median = int(median)
        
    
    #Outputting min max sum avg median using formatting that accounts for right aligning the prices and giving all of the prices decimal and commas
    print(f'{"Minimum":<20} {priceList[0]:>20,.2f}')
    print(f'{"Maximum":<20} {priceList[-1]:>20,.2f}')
    print(f'{"Sum":<20} {sum(priceList):>20,.2f}')
    print(f'{"Avg":<20} {average:>20,.2f}')
    print(f'{"Median":<20} {priceList[median]:>20,.2f}\n')

    #Indexing the keys from the property types dictionary and summing their price values
    print(f'Summary by Property Type: ')
    print(f'{"Residential":<20} {sum(propDict["Residential"]):>20,.2f}')
    print(f'{"Condo":<20} {sum(propDict["Condo"]):>20,.2f}')
    print(f'{"Multi-Family":<20} {sum(propDict["Multi-Family"]):>20,.2f}')
    print(f'{"Unkown":<20} {sum(propDict["Unkown"]):>20,.2f}\n')

    #Creates for loops for the zip code and city dictionaries to output them quickly using a for loop
    print(f"\nSummary by zip codes: ")
    for key in zipDict:
        print(f'{key.title():<20} {sum(zipDict[key]):>20,.2f}')
    print(f'\nSummary by city: ')
    for key in cityDict:
        print(f'{key.title():<20} {sum(cityDict[key]):>20,.2f}')

    

main()
