import random
from game_data import data
from art import logo, vs
import os

def show_account(account):
    return f"{account["name"]}, {account["description"]}, from {account["country"]}" 

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct"""
    if a_followers > b_followers :
        return guess == "a"
    else:
        return guess == "b"

def clear_screen():
    os.system('clear')

def game():
    print(logo)
    account_b = random.choice(data)
    score = 0
    while True:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {show_account(account_a)}")
        print(vs)
        print(f"Agains B: {show_account(account_b)}")

        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        is_correct = check_answer(guess,a_follower,b_follower)

        clear_screen()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right. Current score: {score}")
        else:
            score = score
            print(f"You're wrong. Current score: {score}")
            return
        
        ans = input("Do you want to play again? Type 'y' or 'n': ")
        if ans == "n":
            return
    
game()



