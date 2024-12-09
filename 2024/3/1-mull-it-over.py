import re
file = open("input.txt")
text = file.read()

result = 0

x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", text)
for m in x:
    m = m.replace("mul(","").replace(")","").split(',')
    result += int(m[0]) * int(m[1])
    
print(result)