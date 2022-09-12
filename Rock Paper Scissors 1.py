import random
while True:
    
    Player = input()
    Computer = random.randint(0,2)

    if Computer == 0:
        Computer = "Rock"
    if Computer == 1:
        Computer = "Paper"
    if Computer == 2:
        Computer = "Scissors"

    print("Oliver chooses " + Player)
    print("----")
    print("Computer chooses:" + Computer)

    if Player == Computer:
        print("Ops, it's a Draw")
    else:
        if Player == "Rock":
            if Computer == "Paper":
                print("You Lose :(")
            else:
                Computer == "Scissors"
                print("Congrats, You Win!")
                
        
        elif Player == "Paper":
            if Computer == "Rock":
                print("Yay, you win")
            else:
                Computer == "Scissor"
                print("You loseee!")    
            
            
        elif Player == "Scissors":
            if Computer == "Paper":
                print("Marvelous! You're the man!")
            else:
                Computer == "Rock"
                print("Chicken dinner, you lose")
        
        else:
            print("Sorry, Wrong input!!!") 
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break