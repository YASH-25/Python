import os

class intelligencer:
    def __init__(self, codelist):
        self.codelist = codelist

    def decode(self):
        numList = []
        li = self.codelist.split(" ")
        for i in li:
            for j in i:
                if j.isdigit():
                    num = j
                    numList.append(int(num))
        wordString = ''.join([i for i in self.codelist if not i.isdigit()])
        wordsList = wordString.split(" ")
        for i in range(len(numList)):
            for j in range(i + 1, len(numList)):
                if (numList[i] > numList[j]):
                    temp = numList[i]
                    temp2 = wordsList[i]
                    numList[i] = numList[j]
                    wordsList[i] = wordsList[j]
                    numList[j] = temp
                    wordsList[j] = temp2
        arrangedSentence = " ".join(wordsList)
        print("DECODED CODE : {}\n".format(arrangedSentence))
        input("\n\nPress any key to continue......")


while True:
    secret_code = input("ENTER SECRET CODE : ")
    li = secret_code.split(" ")
    for i in li:
        count = 0
        for j in i:
            if j.isdigit():
                count = count + 1
        if (count == 0 or count > 1):
            print("the secretcode is invalid\n")
            break
    if (count == 1):
        obj = intelligencer(secret_code)
        obj.decode()



