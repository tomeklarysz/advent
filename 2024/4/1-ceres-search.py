file = open("input.txt")
lines = file.readlines()
file.close()
file = open("input.txt")

def isXmas(c1, c2, c3, c4):
	if c1 + c2 + c3 + c4 == 'XMAS':
		return True
	return False

result = 0

length = len(lines)
print(length)
for i in range(length):
	line = lines[i]
	lineLen = len(line)
	for j in range(lineLen - 1):
		# horizontal
		# normal
		if j < lineLen - 4 and isXmas(line[j], line[j+1], line[j+2], line[j+3]):
			result += 1
		# backwards
		if j > 2 and isXmas(line[j], line[j-1], line[j-2], line[j-3]):
			result += 1
		
		# vertical
		# down
		if i < length - 3 and isXmas(line[j], lines[i+1][j], lines[i+2][j], lines[i+3][j]):
			result += 1
		# up
		if i > 2 and isXmas(line[j], lines[i-1][j], lines[i-2][j], lines[i-3][j]):
			result += 1
		
		# diagonal
		# top left
		if i >= 3 and j >= 3:
			# bottom to top
			if isXmas(line[j], lines[i-1][j-1], lines[i-2][j-2], lines[i-3][j-3]):
				result += 1
		# top right
		if i >= 3 and j < lineLen - 4:
			# bottom to top
			if isXmas(line[j], lines[i-1][j+1], lines[i-2][j+2], lines[i-3][j+3]):
				result += 1
		# bottom right
		if i < length - 3 and j < lineLen - 4:
			# top to bottom
			if isXmas(line[j], lines[i+1][j+1], lines[i+2][j+2], lines[i+3][j+3]):
				result += 1
		# bottom left
		if i < length - 3 and j >= 3:
			# top to bottom
			if isXmas(line[j], lines[i+1][j-1], lines[i+2][j-2], lines[i+3][j-3]):
				result += 1

print(result)