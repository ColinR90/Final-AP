global Election_Candidates
global Election_Regions
global Election_Parties
Election_Parties = input("Input amount of election Political Parties:")
Election_Candidates = input("input amount of candidates:")
Election_Regions = input("input amount of electoral regions:")
class Candidate :
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
    


