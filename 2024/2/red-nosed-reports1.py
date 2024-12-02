safeReports = 0
count = 0
with open("input.txt", "r") as f:
    count = 0
    for line in f:
        isSafe = True
        l = line.split()
        
        incr = False
        decr = False
        if int(l[0]) < int(l[1]):
            incr = True
        elif int(l[0]) > int(l[1]):
            decr = True
        else:
            pass
        
        for i in range(len(l) - 1):
            if incr:
                val = int(l[i+1]) - int(l[i])
            else:
                val = int(l[i]) - int(l[i+1])
            if not (val >= 1 and val <= 3):
                isSafe = False
                break
    
        if isSafe:
            safeReports += 1
        count += 1
        
print(safeReports)    