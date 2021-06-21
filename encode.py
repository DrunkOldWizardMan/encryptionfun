import os
import random
def hexadecimalencode(a):
    conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    a_list = []
    aint = int(a)
    while aint != 0:
        add = aint % 16
        a_list.append(add)
        aint //= 16
    list.reverse(a_list)
    output = ""
    for digit in a_list:
        time = 0
        for step in conversion:
            if digit == time:
                output += step
                break
            else:
                time += 1
    return output
def base64decode(code):
    base64list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f",
                    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                    "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1",
                    "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
    alist = []
    blist = []
    finalnumber = 0
    for char in code:
        alist.append(char)
    list.reverse(alist)
    for variable in alist:
        time = 0
        for key in base64list:
            if key == variable:
                blist.append(time)
                break
            else:
                time +=1
    timesran = 0
    for x in blist:
        power = 64 ** timesran
        finalnumber += x * power
        timesran += 1
    return finalnumber
f = open("seed.txt", "r")
seed = base64decode(f.read())
f.close()
list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", " "]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,]
random.seed(seed)
random.shuffle(list_1)
random.shuffle(list_2)
tuplelist = list(zip(list_1, list_2))
input = open("input.txt", "r")
list_a = []
list_b = []
list_c = []
for text in input.read():
    list_a.append(text.lower())
for char in list_a:
    for key, value in tuplelist:
        if key == char:
            list_b.append(value)
            break
for numbers in list_b:
    list_c.append(hexadecimalencode(numbers))
os.remove("output.txt")
output = open("output.txt", "a")
for hex in list_c:
    output.write(hex)
    output.write("\n")
output.close()
input.close()