from random import randint
print("Put these on yer knuckles")

adjectives = []

#First things first, we need to open up a file and read each one into a list
def openFile(filename):
    with open (filename) as f:
        return f.read().splitlines()

    # with open ('fourLetterNouns.txt') as f:
    #     nouns = f.read().splitlines()
    #
    # with open ('fourLetterAdjective.txt') as f:
    #     adjectives = f.read().splitlines()
    #
    # with open ('fourLetterAdverb.txt') as f:
    #     adverbs = f.read().splitlines()

    # print(verbs, nouns, adjectives, adverbs)
def generateTats():
    #Open files
    words = openFile('fourLetterNouns.txt') + openFile('fourLetterAdverb.txt') + openFile('fourLetterVerbs.txt') + openFile('fourLetterAdjective.txt')

    #grab first words
    print len(words)

    #grab seond words


    #print out as one lines


    #print a list of the contents of the file

generateTats()
