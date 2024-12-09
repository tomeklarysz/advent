import re
file = open("input.txt")
text = file.read()

result = 0
enabled = True

x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", text)
for m in x:
    if m == "do()":
        enabled = True
        continue
    if m == "don't()":
        enabled = False
        continue
    if enabled:
        m = m.replace("mul(","").replace(")","").split(',')
        result += int(m[0]) * int(m[1])
    
print(result)