with open("Day24/Mail_Merge/Input/Letters/starting_letter.txt") as file:
    data = file.read()

with open("Day24/Mail_Merge/Input/Names/invited_names.txt") as f:
    names = f.readlines()

for name in names:
    strip_name = name.strip()
    new_letter = data.replace("[name]", strip_name)
    with open(f"Day24/Mail_Merge/Output/ReadyTosend/letter_for_{strip_name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)