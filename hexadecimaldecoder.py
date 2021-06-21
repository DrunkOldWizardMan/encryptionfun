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