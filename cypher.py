import os
import re


class Err(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self)

    def printmsg(self):
        input(self.msg)


class MultipleDigitsException(Err):
    def __init__(self, msg="Invalid Inputs Detected!!\n[ NOTE : There should be ONLY one digit per word ]\nTry Again!!\n\nHit <enter_key> to continue ..."):
        super().__init__(msg)


class NoDigitsException(Err):
    def __init__(self, msg="Invalid Inputs Detected!!\n[ NOTE : There should be AT LEAST one digit per word ]\nTry Again!!\n\nHit <enter_key> to continue ..."):
        super().__init__(msg)


class intelligencer:

    def __init__(self, secret_code):
        self.code = secret_code

    def decode(self):
        # To split the string with whitespace as delimiter
        self.code = self.code.split()

        # To arrange the words in correct order based on the digits present in each word
        decoded = [None] * len(self.code)
        for i in self.code:
            numlist = re.findall(r'[\d]', i)
            if len(numlist) == 1:
                decoded[int(numlist[0])-1] = i
            elif len(numlist) == 0:
                raise NoDigitsException
            else:
                raise MultipleDigitsException
        decoded = ' '.join(decoded)

        # To remove all digits from the string
        decoded = re.sub(r'[0-9]', '', decoded)

        return decoded


if __name__ == '__main__':
    while True:
        # os.system('cls')
        secret = input("\nENTER SECRET CODE : ")
        obj = intelligencer(secret)
        try:
            decoded = obj.decode()

        except MultipleDigitsException as MDE:
            MDE.printmsg()
            continue

        except NoDigitsException as NDE:
            NDE.printmsg()
            continue

        print("\nDECODED CODE : ", decoded)
        input("\n\nPress <enter> key to continue ...")
