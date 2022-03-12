import random
sc = ["!", "@", "#", "$", "%", "^", "&", "*",]
num = ["1","2","3","4","5","6","7","8","9","0"]   
def suggest(userName):
    userName = list(userName)
    suggestion = ""
    for i in userName:
        x = random.randint(0,1)
        if(x == 1):
            suggestion += i.upper()
        else:
            suggestion += i.lower()
    scList = list(random.choice(sc) for i in range(3))
    numList = list(random.choice(num) for i in range(3))
    charList = scList + numList
    random.shuffle(charList)
    for i in charList:
        suggestion += i
    
    print("here's a suggesion:" ,suggestion)
if __name__ == '__main__':
    isValid = lambda sc, mPasso, passo : True if not mPas.isdisjoint(set(sc)) and not mPasso.isdisjoint(set(num)) and not passo.isupper() and not passo.islower() and len(passo) > 8 else False
    while True:
        usr = input("\nEnter your username     : ")
        if(len(usr) < 3):
            print("Short user name Please Try again")
            continue
        pas = input("\nEnter your new password : ")
        mPas = set(pas)
            
        if isValid(sc,mPas,pas):
            print("\nStrong Password! Go Ahead and Register.")
        else:
            print("\nWEAK PASSWORD.")
            suggest(usr)