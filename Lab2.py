def googlePassion(inputList):
    sMap = {
        1 : "g",
        2 : "o",
        3 : "l", 
        4 : "e"
    }
    output = ""
    for i in inputList:
        try:
            output = output + sMap[i]
        except:
            if(i == 5 and output != ""):
                temp = output[-1]
                output = output[:-1]
                output = output + temp.upper()
                continue
            elif (i in [6,7,8]):
                continue
            else:
                print("Number not defined")
                break
    if(6 in inputList):
        output = output + "."
    if(7 in inputList): 
        output = output[0].upper() + output[1:]
    if(8 in inputList):
        output = output[::-1]
    print(output)

def linguist(inputList):
    output = ""
    output = inputList[0]
    for i in range(1,len(inputList)):
        currentStr = inputList[i]
        matches = []
        for i in range(len(currentStr)):
            if(currentStr[:i] == output[-i:]):
                matches.append(i)
        if(len(matches) > 0):
            bestMatch = matches[-1]
            output = output[:len(output) - bestMatch] + currentStr 
            matches  = []
        else:
            continue
            matches  = []
    print(output)
        