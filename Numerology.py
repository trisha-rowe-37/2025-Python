#Creates the class for main use in this program
class Numerology:

    #Initializes the 2 pieces of information the user will enter into the class function in the other program.
    #Lets the rest of the class functions use these variables with the self identifier
    def __init__(self, sName, sDOB):
        self.sName = sName
        self.sDOB = sDOB

    #Returns all of the printing to the screen in a neat way with \n and spacing modifies for neatness
    def __str__(self):
        return (f'\nClient Name: {self.sName}\n'
                f'Client DOB: {self.sDOB}\n'
                f'\n'
                f'{"Life Path:":<13} {self.getLifePath():>5}\n'
                f'{"Birthday:":<13} {self.getBirthDay():>5}\n'
                f'{"Attitude:":<13} {self.getAttitude():>5}\n'
                f'{"Soul:":<13} {self.getSoul():>5}\n'
                f'{"Personality:":<13} {self.getPersonality():>5}\n'
                f'{"Power Name:":<13} {self.getPowerName():>5}\n')

    #Basic function that returns the name the user enters
    def getName(self):
        return self.sName

    #Basic function that returns the date of birth the user enters
    def getBirthdate(self):
        return self.sDOB

    #Computes the attitude number by indexing the DOB string assuming its in MM/DD/YYYY format.
    #Only needs to add the month and date together
    #Multiple if statements used just in case the attitude number has 2 digits
    def getAttitude(self):
        att1 = int(self.sDOB[0])
        att2 = int(self.sDOB[1])
        att3 = int(self.sDOB[3])
        att4 = int(self.sDOB[4])
        attitude = str(att1+ att2+ att3+ att4)
        if int(attitude) >= 10:
            att5 = int(attitude[0])
            att6 = int(attitude[1])
            totAtt = att5 + att6
            if totAtt >= 10:
                att7 = int(totAtt[0])
                att8 = int(totAtt[1])
                totAtt2 = att7 + att8
                return totAtt2
            else:
                return totAtt
        else:
            return attitude
        
        
    #Indexes the days of the DOB and adds them together to get the birth day number.
    #If statement used just in case the birth day number has 2 digits
    def getBirthDay(self):
        day1 = int(self.sDOB[3])
        day2 = int(self.sDOB[4])
        day = str(day1 + day2)
        if int(day) >= 10:
            day3 = int(day[0])
            day4 = int(day[1])
            birthDay = day3 + day4
            return birthDay
        else:
            return day

    #Indexes the entire DOB while accounting for skipping the slashes or dashed in the 2nd and 5th indexes.
    #Multiple if statements used once again just in case number is above 10
    def getLifePath(self):
        path1 = int(self.sDOB[0])
        path2 = int(self.sDOB[1])
        path3 = int(self.sDOB[3])
        path4 = int(self.sDOB[4])
        path5 = int(self.sDOB[6])
        path6 = int(self.sDOB[7])
        path7 = int(self.sDOB[8])
        path8 = int(self.sDOB[9])
        path = str(path1 + path2 + path3 + path4 + path5 + path6 + path7 + path8)
        if int(path) >= 10:
            pathed1 = int(path[0])
            pathed2 = int(path[1])
            totPath = str(pathed1 + pathed2)
            if int(totPath) >= 10:
                pathedAgain1 = int(totPath[0])
                pathedAgain2 = int(totPath[1])
                totPath2 = pathedAgain1 + pathedAgain2
                return totPath2
            else:
                return totPath
        else:
            return path
            
        
        
    #Creates strName to put all of the constanants in self.sName in a variable
    #Iterates over self.sName to do this
    #Iterates over strName to determine which constanant group each character belongs in. Proceeds to assign a number to add to tot for each iteration
    #Creates while loop instead of double for loops from earlier using len == 2 to account for double digits instead of >= 10, if total personality and soul are 3 digits use elif len == 3
    def getPersonality(self):
        strName = ""
        for char in self.sName:
            if char.isalpha() == True:
                if char.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
                    strName += char
                else:
                    pass
            else:
                pass
        tot = 0
        for char in strName:
            if char.upper()  in "JS":
                tot += 1
            if char.upper()  in "BKT":
                tot += 2
            if char.upper()  in "CL":
                tot += 3
            if char.upper()  in "DMV":
                tot += 4
            if char.upper()  in "NW":
                tot += 5
            if char.upper()  in "FX":
                tot += 6
            if char.upper()  in "GPY":
                tot += 7
            if char.upper()  in "HQZ":
                tot += 8
            if char.upper()  in "R":
                tot += 9


        while tot >= 10:
            totstring = str(tot)
            if len(totstring) == 2:
                tot = int(totstring[0]) + int(totstring[1])
            elif len(totstring) == 3:
                tot= int(totstring[0]) + int(totstring[1])
        return tot

  
    #Adds the returned value from the getSoul and getPersonality functions to PowerName.
    # Since number should be small, only use one if statemement to account for double digits
    def getPowerName(self):
        Soul = self.getSoul()
        Personality = self.getPersonality()
        PowerName = Soul + Personality
        if PowerName >= 10:
            PowerName = str(PowerName)
            PowerName = int(PowerName[0]) + int(PowerName[1])
            return PowerName
        else:
            return PowerName

    #Same as getPersonality but instead accounting for vowels.
    #Uses same while loop as before
    def getSoul(self):
        strName = ""
        for char in self.sName:
            if char.isalpha() == True:
                if char.upper() in "AEIOU":
                    strName += char
                else:
                    pass
            else:
                pass
        tot = 0
        for char in strName:
            if char.upper() in "A":
                tot += 1
            if char.upper() in "U":
                tot += 3
            if char.upper() in "E":
                tot += 5
            if char.upper() in "O":
                tot += 6
            if char.upper() in "I":
                tot += 9

        while tot >= 10:
            totstring = str(tot)
            if len(totstring) == 2:
                tot = int(totstring[0]) + int(totstring[1])
            elif len(totstring) == 3:
                tot= int(totstring[0]) + int(totstring[1])
        return tot
    
