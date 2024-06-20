import random

#list of char
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to Password Generator")
letter = input("How many letters do you want?\n")
sym = input("How many symbols do you want?\n")
number = input("How many numbers do you want?\n")


if not letter.isdigit() or not sym.isdigit() or not number.isdigit():
    print("Invalid value, please enter the number")
else:
    word = []
    letter = int(letter)
    sym = int(sym)
    number = int(number)

    for i in range(letter):
        char = random.choice(letters)
        word.append(char)

    for i in range(sym):
        symbol = random.choice(symbols)
        word.append(symbol)
    
    for i in range(number):
        num = random.choice(numbers)
        word.append(num)

    random.shuffle(word)
    print("Your pass word is", "".join(word))

    if len(word) <= 6:
        print("Your password is weak, try to include at least 8 characters for a stronger password.")
    elif len(word) == 7:
        print("Your password is medium, try to include at least 8 characters for a stronger password.")
    else:
        print("Your password is strong.")

