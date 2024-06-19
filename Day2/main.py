print("Welcome to the tip calculato")
bill = float(input("What is the total bill amount?($) \t"))
tip = float(input("How much tip would you like to give?(%) \t"))
person = int(input("How many people to split the bill? \t"))
print("Each person have to pay: ", (bill*tip/100 + bill)/person)


