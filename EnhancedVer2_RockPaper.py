#### Rock Paper Scissors Game. Version 2 (20 lines)
print("Instruction: 0 means Rock; 1 means Paper; 2 means Scissors. Please choose accordingly, have fun!")

import random
while True:

    Player = int(input())
    Computer = random.randint(0,2)

    print("You choose " + str(Player))
    print("----")
    print("Computer chooses "+ str(Computer))

    if Player == Computer:
        print("Tie")
    else:
        #Important! If choose Scissors, it will be 3/3 remainer = 0; Computer chooses 0-rock => Lose
        if (Player + 1) % 3 == Computer:  
            print("You lose!")
        else:
            print("Congrats! You're a winner")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y": 
        break
                                                ## Ollie
