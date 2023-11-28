
with open("chapter_1.txt") as f:
    content = f.readlines()

# join two part words that splitted into 2 line

for i in range(1, len(content)+1):
    print(i, content[i])
