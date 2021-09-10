import sys,random
print("Welcome to the SILLY NAME GENERATOR.\n")

First=('Christopher','Xavier', 'Boggart', 'Plop', 'Wulfrus', 'Wandy', 'Charmayanne', 'Charcole', 'Anomaly', 'Dwarren', 'Prof.')
Last=('Jenks','Troteville', 'Hilton', 'Algernon', 'Curupaa', 'Goon', 'Bubbly', 'Mauii', 'Charcoal', 'The Animal', 'Shufflebottom', 'Shellaberger', 'Stopme', 'The Nidduring', 'Boef', 'Barf',
      'Whooed', 'Areyoustuchha', 'Mydadaa', 'Gans', 'Glancing')
while True:
 FirstName= random.choice(First)
 LastName= random.choice(Last)
 print("\n\n")
 print("{} {}".format(FirstName, LastName),file=sys.stderr)
 tryagain = input("\n\n\n Try it out again?? (Press enter else e to quit)\n\n")
 if tryagain.lower() == "e":
     break
input("Press Enter to exit.")

