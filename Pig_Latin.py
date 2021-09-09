import sys 
Vowel= 'aeiouy'
while True:
    word= input("Type a word to find out it's Pig Latin Translation:")
    if word[0] in Vowel:
        Pig_Latin= word + 'way'
    else:
        Pig_Latin= word[1:] + word[0] + 'ay'
    print("{}".format(Pig_Latin),file=sys.stderr)
    Try_A= input("Press N to exit else enter to try again:")
    if Try_A.lower()== "n":
        sys.exit()