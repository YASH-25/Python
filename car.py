import os


def addv():
    owner = input("\n\nOWNER NAME : ")
    brand = input("CAR BRAND : ")
    model = input("CAR MODEL : ")
    type = input("TYPE OF CAR : ")
    fuel_tank_size = int(input("FUEL TANK SIZE (in litres) : "))
    fuel_level = int(input("CURRENT FUEL LEVEL (in litres) : "))
    if 0 <= fuel_level <= fuel_tank_size:
        return vehicle(owner, brand, model, type, fuel_tank_size, fuel_level)
    else:
        input(
            "\nInvalid Input!\n(Fuel level cannot be greater than fuel tank size or less than 0!!!)\n(Fuel tank size cannot be less than 0!!!)\nFAILED TO APPEND VEHICLE.")
        return []


def selectv(vehicles):
    while True:
        print("\n")
        for i in range(len(vehicles)):
            print((i+1), " ==> ", vehicles[i].o)
        try:
            index = int(
                input("\n\nENTER THE NUMBER ASSOCIATED TO THE OWNER : ")) - 1
            if vehicles[index]:
                return index
        except:
            print("\nINVALID INPUT!\nTRY AGAIN :(")


def print_one(vehicles):
    index = selectv(vehicles)
    obj = vehicles[index]
    print("\nOWNER\t\tBRAND\tMODEL\tTYPE\tFUEL TANK SIZE\tCURRENT FUEL LEVEL")
    print("==========================================================================\n")
    print(obj.o, "\t", obj.b, "\t", obj.m, "\t", obj.t,
          "", obj.fts, "litres \t", obj.fl, "litres \n")
    if obj.fl <= 3:
        print("\nWARNING!\nFUEL LEVEL IS LOW.\nREFILL ASAP!!!!")
    else:
        obj.drive()


def print_all(vehicles):
    print("\nOWNER\t\tBRAND\tMODEL\tTYPE\tFUEL TANK SIZE\tCURRENT FUEL LEVEL")
    print("==========================================================================\n")
    for obj in vehicles:
        print(obj.o, "\t", obj.b, "\t", obj.m, "\t", obj.t,
              "", obj.fts, "litres \t", obj.fl, "litres \n")
        if obj.fl <= 3:
            print("\nWARNING!\nFUEL LEVEL IS LOW.\nREFILL ASAP!!!!")
        else:
            obj.drive()


def print_fuel_level(vehicles):
    index = selectv(vehicles)
    obj = vehicles[index]
    print("\nCURRENT FUEL LEVEL OF ", obj.o,
          "'S VEHICLE IS : ", obj.fl, " litres")
    if obj.fl <= 3:
        print("\nWARNING!\nFUEL LEVEL IS LOW.\nREFILL ASAP!!!!")


def fill_vehicle(vehicles):
    index = selectv(vehicles)
    obj = vehicles[index]
    if not obj.isfull():
        print("\nYOU HAVE SELECTED ", obj.o, "'s VEHICLE.")
        choice = input("\nLET'S REFILL THE FUEL??? (y/n) : ").upper()
        if choice[:1] == "Y":
            print("\nCURRENT FUEL LEVEL IS : ", obj.fl, " litres")
            print("\nVEHICLE'S MAX FUEL LEVEL IS : ", obj.fts, " litres")
            refill = int(input("\nHOW MUCH LITERS DO YOU WANT TO FILL? ? ? : "))
            obj.get_fuel(refill)
    else:
        print("\nTANK IS FULL!!")
    vehicles[index] = obj
    return vehicles


class vehicle:
    def __init__(self, owner, brand, model, type, fuel_tank_size, fuel_level):
        self.o = owner
        self.b = brand
        self.m = model
        self.t = type
        self.fts = fuel_tank_size
        self.fl = fuel_level

    def isfull(self):
        if self.fl == self.fts:
            return True
        else:
            return False

    def update_fuel_tank(self, newlevel):
        self.fl += newlevel
        if self.fl <= 3:
            print("\nWARNING!\nFUEL LEVEL IS LOW.\nREFILL ASAP!!!!")


    def get_fuel(self, refill):
        if self.fl + refill > self.fts:
            print("\nWARNING!\nFUEL LEVEL IS EXCEEDING TANK CAPACITY!!!!\n",
                  (self.fl + refill - self.fts), "litres of fuel will not be needed.")
            self.fl = self.fts
        else:
            self.update_fuel_tank(refill)

    def drive(self):
        print("WOW!,", self.o, " IS DRIVING :)))))), ", self.b, " ", self.m)


if __name__ == '__main__':
    vehicles = []
    while True:
        #os.system('cls')
        print("( 1 ) : to APPEND to the list of vehicles")
        print("( 2 ) : to PRINT details of a specific vehicle")
        print("( 3 ) : to PRINT details of all vehicles")
        print("( 4 ) : to GET FUEL LEVEL of a vehicle")
        print("( 5 ) : to REFILL a vehicle")
        print("( 6 ) : to DELETE ALL entries")
        print("( 0 ) : to EXIT")
        ch = input(" -->  : ")

        if ch != '1' and ch != '6' and ch != '0' and vehicles == []:
            input(
                "\nSORRY THERE IS NO VEHICLE IN THE LIST.\nAPPEND SOME VEHICLE DETAILS AND TRY AGAIN!!!")
        else:
            if ch == '1':
                temp = addv()
                if temp != []:
                    vehicles.append(temp)
                input("\nPress any key to continue ...")

            elif ch == '2':
                print_one(vehicles)
                input("\nPress any key to continue ...")

            elif ch == '3':
                print_all(vehicles)
                input("\nPress any key to continue ...")

            elif ch == '4':
                print_fuel_level(vehicles)
                input("\nPress any key to continue ...")

            elif ch == '5':
                vehicles = fill_vehicle(vehicles)
                input("\nPress any key to continue ...")

            elif ch == '6':
                vehicles = []
                input(
                    "\nAll entries have been deleted successfully!\nPress any key to continue ...")

            elif ch == '0':
                exit()

            else:
                input("WRONG INPUT!!\nTRY AGAIN!!")
