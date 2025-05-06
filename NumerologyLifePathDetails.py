from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):

    def __init__(self, sName, sDOB):
        super().__init__(sName, sDOB)

    @property
    def LifePathDescription(self):
        lifepath = int(self.LifePath)
        lifepathdict = {1:"The Independent: Wants to work/think for themselves",
                        2:"The Mediator: Avoids conflict and wants love and harmony",
                        3:"The Performer: Likes music, art and to perform or get attention",
                        4:"The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
                        5:"The Adventurer: Likes to travel and meet others, often a extrovert",
                        6:"The Inner Child: Is meant to be a parent and/or one that is young at heart",
                        7:"The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
                        8:"The Executive: Gravitates to money and power",
                        9:"The Humanitarian: Helps others and/or experiences pain and learns the hard way"}
        return lifepathdict[lifepath]

    def __str__(self):
        return (f'\nClient Name: {self.Name}\n'
                   f'Client DOB: {self.Birthdate}\n'
                   f'\n'
                   f'{"Life Path:":<13} {self.LifePath:>5}\n'
                   f'Life Path Description: {self.LifePathDescription}\n'
                   f'{"Birthday:":<13} {self.BirthDay:>5}\n'
                   f'{"Attitude:":<13} {self.Attitude:>5}\n'
                   f'{"Soul:":<13} {self.Soul:>5}\n'
                   f'{"Personality:":<13} {self.Personality:>5}\n'
                   f'{"Power Name:":<13} {self.PowerName:>5}\n')


    @property
    def Name(self):
        return self.getName()

   
    @property
    def Birthdate(self):
        return self.getBirthdate()


    @property
    def Attitude(self):
        return self.getAttitude()
        
        

    @property
    def BirthDay(self):
        return self.getBirthDay()


    @property
    def LifePath(self):
        return int(self.getLifePath())
            
        
        
    @property
    def Personality(self):
        return self.getPersonality()

  
    @property
    def PowerName(self):
        return self.getPowerName()


    @property
    def Soul(self):
        return self.getSoul()

