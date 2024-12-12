file = open("input.txt")
lines = file.readlines()
file.close()
file = open("input.txt")

def isXmas(topleft, topright, botright, botleft):
    if topleft == 'M':
        if not botright == 'S':
            return False
    if topleft == 'S':
        if not botright == 'M':
            return False
    if topright == 'M':
        if not botleft == 'S':
            return False
    if topright == 'S':
        if not botleft == 'M':
            return False
    return True

result = 0

length = len(lines)

for i in range(length):
    if (i == 0 or i == length - 1):
        continue
    line = lines[i]
    lineLen = len(line)
    for j in range(lineLen - 1):
        if (j == 0 or j == lineLen - 2):
            continue
        if not line[j] == 'A':
            continue
        topleft = lines[i-1][j-1]
        if topleft != 'M' and topleft != 'S':
            continue
        topright = lines[i-1][j+1]
        if topright != 'M' and topright != 'S':
            continue
        botright = lines[i+1][j+1]
        if botright != 'M' and botright != 'S':
            continue
        botleft = lines[i+1][j-1]
        if botleft != 'M' and botleft != 'S':
            continue
        if isXmas(topleft, topright, botright, botleft):
            result += 1

print(result)