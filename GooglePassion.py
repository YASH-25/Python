def gp(inp):
    d = {"1": "g", "2": "o", "3": "l", "4": "e"}
    temp = ""
    dot = 0
    ch = '12345678'
    for i in inp:
        if i in ch:
            if i == '1' or i == '2' or i == '3' or i == '4':
                temp = temp + d[i]
            elif i == '5' and temp != "":
               temp2 = temp[-2:]
               temp = temp[:-2]
               temp = temp + temp2.capitalize()
            elif i == '6':
                dot = dot + 1
            elif i == '7':
                temp = temp.capitalize()
            elif i == '8':
                temp = temp[::-1]
            pass

            while dot:
                temp = temp + '.'
                dot = dot - 1
        else:
            print("INVALID CHARACTER DETECTED!\nPROGRAM WILL TERMINATE.")
            return

    return temp


if __name__ == '__main__':
    print("1:g, 2:o, 3:l, 4:e")
    print("5 indicates to up case of letter before it.")
    print("6 indicates Add a point to the end.")
    print("7 indicates Change case of the first letter.")
    print("8 indicates Reverse the string.")
    inp = input("\n[->] Enter your input: ")
    final_str = gp(inp)
    print(final_str)
