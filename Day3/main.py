print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

ans = input("Left or right? \t")
if ans.lower() == "right":
    print('''                      -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
  ''')
    
    print("Sonic got the treasure before you, try again.")
else:
    print('''
   _                                                           
  | |                                                          
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                        | |    
                                                        |_| 
  ''')
    print("Nice, you made it to the next level!")

    ans2 = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.\nType Swim/Wait: ").lower()
    if ans2 == "swim":
        print('''
                    (`.
                    \ `.
                      )  `._..---._
    \`.       __...---`         o  )
    \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
    /,'    ``--.._____\/--''
        ''')
        print("Unfortunately, you were eaten by a Great White Shark, try again.")
    
    elif ans2 == "wait":
        print("Nice, you made it to the next level, you're pretty good at this!")
        print ("Welcome to:")
        print ('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    ''')
        ans3= input("Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()
        if ans3== "dig":
            print("You've found the treasure, you win!")
        elif ans3 == "cave":
            print('''
      _                     
      | |                    
      | |__   ___  __ _ _ __ 
      | '_ \ / _ \/ _` | '__|
      | |_) |  __/ (_| | |   
      |_.__/ \___|\__,_|_|   
                  ''')
        print("You were eaten by a bear, game over.")