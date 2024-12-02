safeReports = 0
count = 0
with open("input.txt", "r") as f:
    count = 0
    for line in f:
        l = line.split()
        isSafe = True
        
        incr = False
        decr = False
        if int(l[0]) < int(l[1]):
            incr = True
        elif int(l[0]) > int(l[1]):
            decr = True
        else:
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
            continue

        isAnySafe = False
        for j in range(len(l)):
            l_copy = l.copy()
            l_copy.pop(j)
            current = True
            
            # if it's increasing
            for i in range(len(l_copy) - 1):
                val = int(l_copy[i+1]) - int(l_copy[i])
                if not (val >= 1 and val <= 3):
                    current = False
                    break
            if current:
                isAnySafe = True
                break
            
            current = True
            # if it's decreasing
            for i in range(len(l_copy) - 1):
                val = int(l_copy[i]) - int(l_copy[i+1])
                if not (val >= 1 and val <= 3):
                    current = False
                    break
            if current:
                isAnySafe = True
                break

        if isAnySafe:
            safeReports += 1
        count += 1
        
print(safeReports)