morse = ['.-', '-..', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
         '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
         '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
         '---..', '----.', '-----', '.-.-.-', '--..--', '..--..', '-.-.--', '.----.',
         '.-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-..-.', '..--.-', '-...-',
         '.-.-.', '-....-', '...-..-', '.--.-.', '---'
         ]

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '.', ',', '?', '!', '`', '"', '(', ')', '&',
        ':', ';', '/', '_', '=', '+', '-', '$', '@'
        ]

# using zip to create two different dictionaries for converting words to morse and vice versa
tochar = dict(zip(morse, char))
tomorse = dict(zip(char, morse))

# to convert from words to morse


def encrypt(in_list):
    out = ""
    for i in in_list:
        for j in i:
            out += tomorse[j]
            out += " "
    print(out)


def decrypt(in_list):  # to convert from morse to words
    out = [tochar[i] for i in in_list]  # use of list comprehension
    x = ""
    for i in out:
        x += i
    print(x)


def check(text):  # to check whether the input is words or morse
    text = text.replace(".", "")
    text = text.replace("-", "")
    text = text.replace(" ", "")
    if(len(text) == 0):
        return "morse"
    else:
        return "words"


if __name__ == '__main__':
    while True:
        print("\n Enter your text: ")
        text = input("\n ->  : ")
        ch = check(text)
        if ch == 'words':
            encrypt(text.lower().split(" "))
        elif ch == 'morse':
            decrypt(text.lower().split(" "))
        