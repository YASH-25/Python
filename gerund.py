import os

def gerund(my_in):
    if(my_in[-3:] == "ing"):
        print("To " + my_in[:-3] + "\n")
    else:
        print("Not a Gerund \n")

if __name__=="__main__":
    os.system('cls')
    my_in = input("Enter your input: ")
    gerund(my_in)