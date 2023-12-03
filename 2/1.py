f = open("2/input.txt", "r")

# 12 red, 13 green, 14 blue
# there are 100 games
sum = 0
index = 1
for i in f:
    text = ""
    text = i.replace("Game ", "")
    text = text.split(";")
    number = int(text[0][0])
    if index == 100: text[0] = text[0][4:]
    else: text[0] = text[0][3:]
    done = False
    print(index)
    index += 1
    print(text)
    
    for x in text:
        x = x.split(",")
        for y in x:
            if done == True: break
            y = y.split()
            if int(y[0]) > 11:
                if y[1] == 'red':
                    done = True
                    break
                elif y[1] == 'green' and int(y[0]) > 12:
                    done = True
                    break
                elif y[1] == 'blue' and int(y[0]) > 13:
                    done = True
                    break
        if done == True: break
        sum += number
        print("sum: "+str(sum))
        break

# print(number)

# print(text)

print(sum)
f.close()