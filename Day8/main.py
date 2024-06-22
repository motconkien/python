from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_text += alphabet[new_position]
        else:
            new_text += char
    print(f"The {direction}d text is {new_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))

    shift = shift % 26 #nếu mà shift < 26 thì sẽ không chia được nên shift dữ nguyên
    caesar(text,shift,direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if result == "no":
        print("Good bye")
        break
    
        
