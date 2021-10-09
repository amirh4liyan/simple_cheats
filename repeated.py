import argparse

# make parser object
parser = argparse.ArgumentParser()


# add arguments here:
parser.add_argument('path', help='the base')
parser.add_argument('-a', '--alphabetic', action='store_true',
                        help='alphabetic order while sorting')
parser.add_argument('-o', '--output',
                        help='place the output there by <name>.txt')
parser.add_argument('-r', '--reverse', action='store_true',
                        help ='reverse order while sorting')


# get data from command-line with parse_arge() method
args = parser.parse_args()
filePath = args.path
isAlpha = args.alphabetic
isReverse = args.reverse
output = args.output

with open("junks.txt") as f:
    content = f.readlines()

junks = []
for j in content:
    junks.append(j.strip('\n'))

strips, spaces, nothing = junks
strips = strips[6:]
spaces = spaces[6:]
nothing = nothing[8:]

def clearText(strLine):
    for case in nothing:
        strLine = strLine.replace(case, '')
    for case in spaces:
        strLine = strLine.replace(case, ' ')
    return strLine

def addKeys(key):
    key = key.strip(strips)
    key = key.lower()
    if len(key) > 2:
        if key not in words:
            words[key] = 1
        else:
            words[key] += 1

words = dict()
with open(filePath) as f:
    while True:
        line = f.readline()

        if line == '':
            break  

        line = clearText(line)
        line = line.split()
        for word in line:
            addKeys(word)

print()
keyWords = list()
for w in words:
    print(w, words[w])
