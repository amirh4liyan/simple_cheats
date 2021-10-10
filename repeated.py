import argparse

# make parser object
parser = argparse.ArgumentParser()


# add arguments here:
parser.add_argument('path', help='the base')
parser.add_argument('-a', '--alphabetic', action='store_true',
                        help='alphabetic order while sorting')
parser.add_argument('-l', '--length',
                        help='define limit for the words')
parser.add_argument('-o', '--output',
                        help='place the output there by <name>.txt')
parser.add_argument('-r', '--reverse', action='store_true',
                        help ='reverse order while sorting')


# get data from command-line with parse_arge() method
def init()
    args = parser.parse_args()
    filePath = args.path
    isAlpha = args.alphabetic
    isReverse = args.reverse
    outputName = args.output

    lLength = 3
    rLength = 16
    if args.length:
        l = args.length[:args.length.index(':')]
        if l:
            lLength = int(args.length[:args.length.index(':')])

        r = args.length[args.length.index(':')+1:]
        if r:
            rLength = int(args.length[args.length.index(':')+1:])

    with open('configs.txt') as f:
        data = f.readlines()

    configs = []
    for j in data:
        configs.append(j.strip('\n'))

    strips, spaces, nothing = configs
    strips = strips[6:]
    spaces = spaces[6:]
    nothing = nothing[8:]

def clearLine(strLine):
    for case in nothing:
        strLine = strLine.replace(case, '')
    for case in spaces:
        strLine = strLine.replace(case, ' ')
    return strLine

def addKeys(keyWord):
    keyWord = keyWord.strip(strips)
    keyWord = keyWord.lower()
    if lLength <= len(keyWord) < rLength:
        if keyWord not in wordsDict:
            wordsDict[keyWord] = 1
        else:
            wordsDict[keyWord] += 1

init()

wordsDict = dict()
with open(filePath) as f:
    while True:
        line = f.readline()

        if line == '':
            break  

        line = clearLine(line)
        line = line.split()
        for word in line:
            addKeys(word)

print()
'''
keyWords = list(wordsDict.keys()[0])
valueWords = list(wordsDict.values()[0])
for key in wordsDict:
    if wordsDict[key] >= valueWords[0]:
        valueWords.insert(0, wordsDict[key])
        keyWords.insert(0, key)
    elif wordsDict[key] < valueWords[0]:
        for i in range(1, len(valueWords)+1):
            if wordsDict[key] >= valueWords[i]:
                valueWords.insert(i, wordsDict[key])
                keyWords.insert(i, key)
print(keyWords)
print(valueWords)
'''
print(wordsDict)
