from art import logo

print(logo)

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": multiple,
    "/": divide
}
def calculator():
    n1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from line above: ")
        n2 = float(input("What is the second number? "))
        calculation = operations[operation_symbol]
        answer = calculation(n1,n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        ans = input(f"Type 'y' to continue with {answer} or type 'n' to exit or tyoe 'new' to start a new calculator: ")
        if ans == "y":
            n1 = answer
        elif ans == "new":
            calculator()
            should_continue = False
        elif ans == "n":
            should_continue = False
            print("Good bye")
        else:
            print("Invalid answer")
            should_continue = False
            print("Good bye")
            
calculator()