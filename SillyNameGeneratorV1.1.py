import sys,random
print("Welcome to the SILLY NAME GENERATOR.\n")
#Names
First=('Christopher','Xavier', 'Boggart', 'Plop', 'Wulfrus', 'Wandy', 'Charcole', 'Anomaly', 'Tenysi', 'StrikingDuck', 'Dwarren', 'Prof.')
#Middle Names
Middle=('Andy','Marquee','MacnCheese','Boom','Rotator','Blame', 'Blimely','Bee','Ballet','wrought')
#SurNames
Last=('Jenks','Troteville', 'Hilton', 'Algernon', 'Goon', 'Bubbly', 'Mauii', 'Charcoal', 'The Animal', 'Shufflebottom', 'Shellaberger', 'Boef', 'Barf','Whooed','iron')
#Created a list to get a random choice(True or False)
TF= ('True','false')
while True:
    #Taking a random name,surname,middle name and choice(For TF)
    MiddleName= random.choice(Middle)
    FirstName= random.choice(First)
    LastName= random.choice(Last)
    truefalse= random.choice(TF)
    if truefalse== 'True':
        print("{} {} {}".format(FirstName,MiddleName, LastName),file=sys.stderr)
    else:   
        print("\n\n")
        print("{} {}".format(FirstName, LastName),file=sys.stderr)
    tryagain = input("\n\n\n Try it out again?? (Press enter else q to quit)\n\n")
    if tryagain.lower() == "q": 
        break
        input("Press enter to exit")
