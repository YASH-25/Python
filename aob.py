import os, re

def aob(inp):
    try:
        int(inp)
        print("Orange")
    except :
        flag = False
        sc = '[+-@_!#$%^&*()<>?/\|}{~:;],."'
        for i in inp:
            if i in sc:
                flag = True
                break
        if flag:
            print("Banana")
        else:
            str(inp)
            print("Apple")

if __name__=="__main__":
    os.system('cls')
    inp = input("Enter your input: ")
    aob(inp)