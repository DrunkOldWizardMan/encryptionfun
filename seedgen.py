import random
def base64(a):
    a_list = []
    base64list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                    "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f",
                    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                    "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1",
                    "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
    aint = int(a)
    while aint != 0:
        add = aint % 64
        a_list.append(add)
        aint //= 64
    list.reverse(a_list)
    output = ""
    for digit in a_list:
        current = digit
        time = 0
        for letter in base64list:
            if current == time:
                output += letter
                break
            else:
                time += 1
    return output
f = open("seed.txt", "w")
seed = random.randint(1, 10000000)
baseseed = base64(seed)
f.write(str(baseseed))
f.close()