from collections import defaultdict

file = open("input.txt")
a, b = [], []
for f in file:
    line = f.split()
    a.append(line[0])
    b.append(line[1])

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(list(left[i:]))
    result.extend(list(right[j:]))
    return result

def mergesort(arr):
    length = len(arr)
    if length == 1:
        return arr
    mid = length // 2
    l = mergesort(arr[:mid])
    r = mergesort(arr[mid:])
    return merge(l, r)

a = mergesort(a)
b = mergesort(b)

# count the distance and fill map
distance = 0
map = defaultdict(int)
for i in range(len(b)):
    distance += abs(int(a[i]) - int(b[i]))
    val = int(b[i])
    map[int(b[i])] += 1

print(distance)

score = 0
for i in range(len(a)):
    score += int(a[i]) * map[int(a[i])]

print(score)