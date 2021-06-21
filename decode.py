import random
import os
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
def hexdecode(a):
    a_list = []
    conversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    b_list = []
    finalnumber = 0
    for char in a:
        a_list.append(char)
    list.reverse(a_list)
    for digit in a_list:
        time = 0
        for step in conversion:
            if step == digit:
                b_list.append(time)
                break
            else:
                time += 1
    timesran = 0
    for x in b_list:
        power = 16 ** timesran
        finalnumber += x * power
        timesran += 1
    return finalnumber
output = open("output.txt", "r")
hexlist = []
for line in output:
    hexlist.append(line.strip("\n"))
output.close()
decodedlist = []
for hex in hexlist:
    decodedlist.append(hexdecode(hex))
f = open("seed.txt", "r")
seed = base64decode(f.read())
f.close()
list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", " "]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,]
random.seed(seed)
random.shuffle(list_1)
random.shuffle(list_2)
tuplelist = list(zip(list_2, list_1))
translatedlist = []
for numbers in decodedlist:
    for key, value in tuplelist:
        if numbers == key:
            translatedlist.append(value)
            break
outputtext = ""
for char in translatedlist:
    outputtext += char
decode = open("decoded.txt", "w")
decode.write(outputtext)
decode.close()