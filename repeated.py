import argparse

# make parser object
parser = argparse.ArgumentParser()


# add arguments here:
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')
parser.add_argument('-v', '--verbosity', action='count', default=0)


# get some data from command-line with parse_arge() method
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print('the square of %d equals %d' %(args.x, answer))
elif args.verbosity >= 1:
    print('%d^%d = %d' %(args.x, args.y, answer))
else:
    print(answer)


'''
# Get text-file path from USER
print('Enter Absolute Path')
print('[if text is in current path, jusu enter the name]')
filePath = input('file path: ')

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
for w in words:
    print(w, words[w])
'''
