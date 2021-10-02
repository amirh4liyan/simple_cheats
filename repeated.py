# Get text-file path from USER
print('Enter Absolute Path\n[if text is in current path, jusu enter the name]')
filePath = input('file path: ')

with open("junks.txt") as f:
    content = f.readlines()

junks = []
for j in content:
    junks.append(j.strip('\n'))

print(junks)
strips = " ;:,"
spaces = ('(', ')', '{', '}', '.', '=', '_', '"')
nothing = ("-", "<", ">", "'", "/", "*", "@", "#", "$")

def clearText(str1):
    for n in nothing:
        str1 = str1.replace(n, '')
    for s in spaces:
        str1 = str1.replace(s, ' ')
    return str1

def addWords(key):
    key = key.strip(strips)
    if key in words:
        words[key] += 1
    else:
        words[key] = 1

words = dict()
with open(filePath, 'r') as f:
    while True:
        line = f.readline()

        if line == '':
            break

        line = clearText(line)
        line = line.split()
        for w in line:
            addWords(w)

print()
print(words)
