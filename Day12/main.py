from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5
def check_number(answer, guess, turns):
    """Check answer against guess. Return the number of attemps remaining"""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

def difficulty():
    level= input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    
def game():
    print("Welcome to: ")
    print(logo)
    print("I'm thinking of a number between 1 and 100, try to guess it")
    turns = difficulty()
    answer = random.randint(1,100)
    print("The correct answer is", answer)
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number")

        guess = int(input("Guess the number: "))
        turns = check_number(answer,guess, turns) #have to the same value which could be subtract
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")

game()


