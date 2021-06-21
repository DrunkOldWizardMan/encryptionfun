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