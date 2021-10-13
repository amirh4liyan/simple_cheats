import argparse

# make parser object
parser = argparse.ArgumentParser()


# add arguments here:
parser.add_argument('path', help='the base')
parser.add_argument('-a', '--alphabetic', action='store_true',
                        help='alphabetic order while sorting')
parser.add_argument('-n', '--noNumber', action='store_true',
                        help='ignore numbers as a key')
parser.add_argument('-r', '--reverse', action='store_true',
                        help ='reverse order while sorting')
parser.add_argument('-o', '--output',
                        help='place the output there by <name>.txt')
parser.add_argument('-l', '--length',
                        help='define limit for the words')


# get data from command-line with parse_arge() method
args = parser.parse_args()
filePath = args.path
isAlpha = args.alphabetic
isReverse = args.reverse
numberNotAllowed = args.noNumber
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
    if not (numberNotAllowed and keyWord.isdigit()):
        keyWord = keyWord.strip(strips)
        keyWord = keyWord.lower()
        if lLength <= len(keyWord) <= rLength:
            if keyWord not in wordsDict:
                wordsDict[keyWord] = 1
            else:
                wordsDict[keyWord] += 1

def compareAlpha(x, y):
    a, b = x, y
    if len(x) > len(y):
        a, b = b, a
    answer = a
    for i in range(len(a)):
        ordX = ord(a[i])
        ordY = ord(b[i])
        if ordX == ordY:
            continue
        elif ordX < ordY:
            break
        elif ordX > ordY:
            answer = b
            break
    if answer == y:
        return True
    elif answer == x:
        return False

def swap():
    keyWords[i], keyWords[i-1] = keyWords[i-1], keyWords[i]
    valueWords[i], valueWords[i-1] = valueWords[i-1], valueWords[i]

def sortByAlpha():
    a = len(keyWords)
    for j in range(a):
        for i in range(a-1, 0, -1):
            # if second was closer, return True, else will return False
            if compareAlpha(keyWords[i-1], keyWords[i]):
                swap()

def sortByRepeat():
    a = len(valueWords)
    for j in range(a):
        for i in range(a-1, 0, -1):
            if valueWords[i] > valueWords[i-1]:
                swap()

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
            

keyWords = list(wordsDict.keys())
valueWords = list(wordsDict.values())

if isAlpha:
    sortByAlpha()
else:
    sortByRepeat()
if isReverse:
    keyWords.reverse()
    valueWords.reverse()

print()
NI = len(max(keyWords, key=len)) + 4
for i in range(len(valueWords)):
    key = keyWords[i]
    val = valueWords[i]
    padding = NI - len(key)
    print('%s' + padding*' ' + '%d' %(key, val))