import os

def DnaToRna(my_in):
    dnaMap = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    a = input("Enter your DNA: ")
    a =  a.upper()
    a = a.replace(" ","")
    output = ""
    flag = True
    for i in a:
        try:
            output = output + dnaMap[i]
        except:
            print("Sequence can only include AGCT \n")
            flag = False
            break
    if(flag):
        print(output + "\n")

if __name__ == '__main__':
   os.system('cls')
   my_in = input("Enter your input: ")
   DnaToRna(my_in)