import pandas as pd

df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")

# for (index,row) in df.iterrows():
#     print(row.letter, row.code)

letter_dict = {row.letter : row.code for (index,row) in df.iterrows()}

def generator_phonetic():
    user_input = input("Your name: ").upper()
    try:
        list_phonetic = [letter_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generator_phonetic()
    else:
        print(list_phonetic)
    
generator_phonetic()