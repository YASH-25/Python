import os
import requests
import random
from datetime import date


class Err(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self)

    def printmsg(self):
        input(self.msg)


class NoInputException(Err):
    def __init__(self, msg="\nHIT <enter_key> TO CONINUE ..."):
        super().__init__(msg)

    def getQuotes(self):
        response = requests.get(
            'https://inspirational-quotes-api.herokuapp.com/quotes')
        json = response.json()
        rand = random.randrange(0, 48)
        return (json[rand]['quote'], json[rand]['source'])

    def printQuote(self, quote):
        print("BEAUTIFUL QUOTE FOR YOU : \n\n")
        print("\"", quote[0], "\"")
        print((" " * (len(quote[0]) - len(quote[1]))), "~ ", quote[1])



class HelpUserException(Err):
    def __init__(self, msg="ENTER DATE OF BIRTH IN dd/mm/yyyy format [ e.g. 01/01/2001 ].\nHIT <enter_key> TO CONTINUE ..."):
        super().__init__(msg)


class IncorrectFormatException(Err):
    def __init__(self, msg="IncorrectFormatError : THE DATE ENTER IS NOT IN THE CORRECT FORMAT.\nHIT <enter_key> TO CONTINUE ..."):
        super().__init__(msg)


class DateRangeException(Err):
    def __init__(self, msg="DateRangeError : THE DATE ENTER IS INVALID.\nHIT <enter_key> TO CONTINUE ..."):
        super().__init__(msg)


class TerminateProgramException(Err):
    def __init__(self, msg="BYE! HOPE YOU RUN THIS PROGRAM AGAIN\nHIT <enter_key> TO CONTINUE ..."):
        super().__init__(msg)


class ZodiacNotFoundException(Err):
    def __init__(self, msg="ZodiacNotFoundError : THERE IS NO ZODIAC SIGN ASSOCIATE TO THE ENTERED DATE OF BIRTH.\nHIT <enter_key> TO ENTERED ..."):
        super().__init__(msg)


class InvalidInputException(Err):
    def __init__(self, msg="InvalidInputError : INVALID INPUT WAS GIVEN. TRY AGAIN!\nHIT <enter_key> TO CONTINUE ..."):
        super().__init__(msg)


def isValidDate(day, month, year):
    day_count_for_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[1] = 29

    return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month-1])


def validateDOB(dob):
    today = date.today()
    curr_day = int(today.strftime("%d"))
    curr_month = int(today.strftime("%m"))
    curr_year = int(today.strftime("%Y"))
    if dob == "":
        raise NoInputException
    elif dob[0] == '?':
        raise HelpUserException
    # Date format check
    elif dob[0].lower() == 'q':
        raise TerminateProgramException
    elif dob[0:2].isnumeric() and dob[3:5].isnumeric() and dob[6:10].isnumeric() and dob[2] == dob[5] == '/' and len(dob) == 10:
        # Date range check
        if isValidDate(int(dob[0:2]), int(dob[3:5]), int(dob[6:10])) and (curr_year-100) < int(dob[6:10]) <= curr_year:
            if int(dob[6:10]) == curr_year and int(dob[3:5]) >= curr_month and int(dob[0:2]) > curr_day:
                raise DateRangeException
            else:
                pass
        else:
            raise DateRangeException
    else:
        raise InvalidInputException


def getZodiac(dob):
    zodiac = ("ARIES", "TAURUS", "GEMINI", "CANCER", "LEO", "VIGRO",
              "LIBRA", "SCORPIO", "SAGITTARUS", "CAPRICON", "AQUARIUS", "PISCES")
    sign = str()
    # Finding the corresponding zodiac sign
    if (int(dob[0:2]) >= 21 and dob[3:5] == '03') or (19 >= int(dob[0:2]) and dob[3:5] == '04'):
        sign = zodiac[0]
    elif (int(dob[0:2]) >= 20 and dob[3:5] == '04') or (20 >= int(dob[0:2]) and dob[3:5] == '05'):
        sign = zodiac[1]
    elif (int(dob[0:2]) >= 21 and dob[3:5] == '05') or (21 >= int(dob[0:2]) and dob[3:5] == '06'):
        sign = zodiac[2]
    elif (int(dob[0:2]) >= 22 and dob[3:5] == '06') or (22 >= int(dob[0:2]) and dob[3:5] == '07'):
        sign = zodiac[3]
    elif (int(dob[0:2]) >= 23 and dob[3:5] == '07') or (22 >= int(dob[0:2]) and dob[3:5] == '08'):
        sign = zodiac[4]
    elif (int(dob[0:2]) >= 23 and dob[3:5] == '08') or (22 >= int(dob[0:2]) and dob[3:5] == '09'):
        sign = zodiac[5]
    elif (int(dob[0:2]) >= 23 and dob[3:5] == '09') or (23 >= int(dob[0:2]) and dob[3:5] == '10'):
        sign = zodiac[6]
    elif (int(dob[0:2]) >= 24 and dob[3:5] == '10') or (21 >= int(dob[0:2]) and dob[3:5] == '11'):
        sign = zodiac[7]
    elif (int(dob[0:2]) >= 22 and dob[3:5] == '11') or (21 >= int(dob[0:2]) and dob[3:5] == '12'):
        sign = zodiac[8]
    elif (int(dob[0:2]) >= 22 and dob[3:5] == '12') or (19 >= int(dob[0:2]) and dob[3:5] == '01'):
        sign = zodiac[9]
    elif (int(dob[0:2]) >= 20 and dob[3:5] == '01') or (18 >= int(dob[0:2]) and dob[3:5] == '02'):
        sign = zodiac[10]
    elif (int(dob[0:2]) >= 19 and dob[3:5] == '02') or (20 >= int(dob[0:2]) and dob[3:5] == '03'):
        sign = zodiac[11]
    else:
        raise ZodiacNotFoundException

    return sign


def getHoroDay():
    hday = input(
        "PLEASE ENTER WHICH DAY'S HOROSCOPE YOU WANT :\n1 => TODAY\n2 => TOMORROW\n3 => YESTERDAY\n[ > ] : ")
    if (hday[0].isnumeric):
        hday = int(hday[0])
        if hday == 1:
            return "today"
        elif hday == 2:
            return "tomorrow"
        elif hday == 3:
            return "yesterday"
        else:
            raise InvalidInputException
    else:
        raise InvalidInputException


def horoscope(sign, day):
    params = (
        ('sign', sign),
        ('day', day),
    )
    response = requests.post(
        'https://aztro.sameerkumar.website/', params=params)
    json = response.json()
    print("\nHoroscope for *[ ", json.get('current_date'), " ]")
    print("Zodiac sign : ", sign)
    print("Date Range : ", json.get('date_range'))
    print("Message : ", json.get('description'))
    print("Compatibility : ", json.get('compatibility'))
    print("Mood : ", json.get('mood'))
    print("Lucky Color : ", json.get('color'))
    print("Lucky Number : ", json.get('lucky_number'))
    print("Lucky Time : ", json.get('lucky_time'))
    print("\n\n*[ This date is provided by the api ]")


if __name__ == '__main__':
    while True:
        os.system('cls')
        zodiac = ""
        try:
            print("#########################################LET'S FIND YOUR HOROSCOPE########################################\n\n")
            print("Other Valid Inputs : <enter_key>, '?', 'q or Q'")
            dob = input("[ ENTER THE DATE OF BIRTH dd/mm/yyyy FORMAT ] : ")
            validateDOB(dob)
            zodiac = getZodiac(dob)
            hday = getHoroDay()

        except NoInputException as NIE:
            quote = NIE.getQuotes()
            NIE.printQuote(quote)
            NIE.printmsg()
            continue

        except HelpUserException as HUE:
            HUE.printmsg()
            continue

        except IncorrectFormatException as IFE:
            IFE.printmsg()
            continue

        except DateRangeException as DRE:
            DRE.printmsg()
            continue

        except TerminateProgramException as TPE:
            TPE.printmsg()
            quit()

        except ZodiacNotFoundException as ZNF:
            ZNF.printmsg()
            continue

        except InvalidInputException as IIE:
            IIE.printmsg()
            continue

        horoscope(zodiac, hday)
        input("\nHIT <enter_key> TO CONTINUE ...")
