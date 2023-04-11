
global Election_Candidates
global Election_Regions
Election_Candidates = input("input amount of candidates:")
Election_Regions = input("input amount of electoral regions:")
class Election_Candidate :
    Name = None
    Age = None
    Party = None
    Political_Opinion_Numeral = None
    Political_Scandals =  None
    Is_incumbent = False
    def __init__(self, Name, Age, Party, Political_Opinion_Numeral, Political_Scandals, Is_incumbent):
        self.name = Name
        self.age = Age
        self.Party = Party
        self.Political_Opinion_Numeral = Political_Opinion_Numeral
        self.Political_Scandals = Political_Scandals
        self.Is_incumbent = Is_incumbent
    
class Electoral_Region:
    Population = None
    Party_Favorability = None
    Political_Favorability = None
    def __init__(self, Population, Party_Favorability, Political_Favorability):
        self.Population = Population
        self.Party_Favorability = Party_Favorability
        self.Political_Favorability = Political_Favorability

def Create_Regions (x) :
  for c in range(1,x) :
    Population = input("Insert Population of Region:")
    Party_Favourability = input ("Insert Party Favourability: ")
    Political_Favourability = input("Insert Political Favourability: ")
    Region = Electoral_Region(Population, Party_Favourability, Political_Favourability)
    #sql command
def Create_Candidates(x):
    for c in range (1,x):
        Name = input("Insert Name")
        Age = input ("Age")
        Political_Party = input("Political Party")
        Political_Opinion_Numeral = input("Insert Politcal Opinion_Numeral (from 1-10, 1 meaning very left leaning and 10 meaning very right leaning):, ")
        Candidate = Election_Candidate(Name, Age, Political_Party, Political_Opinion_Numeral)
    
