import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ans = input(
    """What do you choose? 
        0. Rock
        1. Paper
        2. Scissors
            """)
computer_ans = random.randint(0,2)

if not ans.isdigit() or int(ans) > 2:
    print("Invalid valuem you have to enter number from 0 to 2")
else:
    if int(ans) == 0:
        print(f"Your choice is Rock {rock}")
    elif int(ans) == 1:
        print(f"Your choice is Paper {paper}")
    else:
        print(f"Your choice is Scissors {scissors}")
    

    if computer_ans == 0:
        print(f"Computer choice is Rock {rock}")
        if int(ans) == 0:
            print("That is a draw")
        elif int(ans) == 1:
            print("You win")
        else:
            print("You lose because Scissors win against rock")
    elif computer_ans == 1:
        print(f"Computer choice is Paper {paper}")
        if int(ans) == 0:
            print("You lose, Paper wins against rock.")
        elif int(ans) == 1:
            print("That is draw")
        else:
            print("You win")
    else:
        print(f"Computer choice is Scissors {scissors}")
        if int(ans) == 0:
            print("You win")
        elif int(ans) == 2:
            print("That is draw")
        else:
            print("You lose, Scissors win against paper.")