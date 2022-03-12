import os

if __name__ == '__main__':
    os.system('cls')
    while True:
        print("\n( 1 ) : to place an order")

    elif i < len:
                print("\n\nEnter the details for order no. ", (i+1), ":")
                try:
                    ci = int(input("\n\torder 1  : ").upper())
                    vol = int(input("\n\torder 2 : "))
                    op = int(input("\n\torder 3  : "))
                    typ = int(input("\n\torder 4 : ")[0])
                    typ = typ.upper()
                    if len == 1:
                        ftup = ((ci, vol, op, typ))
                    else:
                        tup1 = ((ci, vol, op, typ),)
                        ftup += tup1
                        del tup1
                    i += 1
                except:
                    del ftup
                    print("INVALID INPUT!\nPROGRAM TERMINATED.")
                    exit()

            print("\nJust to confirm your orders are :")
            input()

            print("\nSYMBOL\tVOLUME\tOFFER PRICE\tTYPE OF ORDER")
            print(
                "======================================================\n")
            i = 0
            while i < len:
                j = 0
                while j < 4:
                    if j == 0:
                        print("\n")
                    print(ftup[i][j], "\t", end="")
                    j += 1
                i += 1

            print("\n")

            i = 0
            total_buy = float()
            total_sell = float()
            while i < len:
                if ftup[i][3] == 'B':
                    total_buy += float(ftup[i][1] * ftup[i][2])

                if ftup[i][3] == 'S':
                    total_sell += float(float(ftup[i][1]) * float(ftup[i][2]))
                i += 1

            print("\nTotal Buy amount : ", total_buy)
            print("\nTotal Sell amount : ", total_sell)
