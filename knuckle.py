print("Put these on yer knuckles")

adjectives = []
verbs = []
nouns = []
adverbs = []

#adjective first
#adverb (maybe noun)
#or verb

#First things first, we need to open up a file and read each one into a list
def openFiles():
    with open ('fourLetterVerbs.txt') as f:
        verbs = f.read().splitlines()
    with open ('fourLetterNouns.txt') as f:
        nouns = f.read().splitlines()
    with open ('fourLetterAdjective.txt') as f:
        adjectives = f.read().splitlines()
    with open ('fourLetterAdverb.txt') as f:
        adverbs = f.read().splitlines()

    # print(verbs, nouns, adjectives, adverbs)
def generateTats():
    

openFiles()
generateTats()
