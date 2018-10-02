from random import randint
print("Put these on yer knuckles")

adjectives = []

#First things first, we need to open up a file and read each one into a list
def openFile(filename):
    with open (filename) as f:
        return f.read().splitlines()

    # print(verbs, nouns, adjectives, adverbs)
def generateTats():
    #Open files
    words = openFile('fourLetterNouns.txt') + openFile('fourLetterAdverb.txt') + openFile('fourLetterVerbs.txt') + openFile('fourLetterAdjective.txt')
    #grab first words
    print len(words)
    wordLength = len(words)-1
    #pick random number
    random = randint(0, wordLength)
    rand2 = randint(0, wordLength)

    word1 = words[random]
    word2 = words[rand2]
    print word1 + " " + word2
