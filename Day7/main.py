import random
from hangman import logo2, logo3, stages
import words

print(logo3)


lives = 6
choose = random.choice(words.word_list)
print(f"The choosen word is {choose}")

display = []
for i in range(len(choose)):
    display += "_"

while True:
    letter = input("Choose your letter: ").lower()
    for position in range(len(choose)):
        if choose[position] == letter:
            display[position] = letter 
    print(" ".join(display))

    if letter not in choose:
        lives -=1
        if lives == 0:
            print("You loose")
            break
        else:
           print(stages[lives])

    if "_" not in display:
        word = "".join(display)
        if word == choose:
            print("You win")
            break
    
 
print(logo2)

