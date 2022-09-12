#Program to convert money From USD to VND
# print("Xin USD: ")
# usd= input()
# vnd= int(usd)*22
# print( str(usd) + " USD=" + str(vnd)+ " k VND")

# Prove math methods   (Ctrl + / to Comment | Ctrl + F1 to Interactive)
print("----")
a=1
b=3
if b>2:
    print("a="+ str(a))
    print("b="+ str(b))

# print("----")
# temp = a
# a=b
# b= temp
# print("a="+ str(a))
# print("b="+ str(b))

#Write a love matching program base on # matched characters
print("----")
def love_matching_guess(name_male,name_female):
    name_male= name_male.lower()
    name_female = name_female.lower()
    count = 0
    for num_char in range(ord('a'),ord('z')+1):
        if (chr(num_char) in name_male) and (chr(num_char) in name_female):
            count = count + 1


    if count== 0 :
        result = "NOPE"
    elif count > 3:
        result = "Future lover"
    elif count == 1 or 2 :
        result = "Friend zone ^.^"
    else: 
        result = "Chicken"
    return result

print("Male Name: ")
name_male= input()
print("Female Name: ")
name_female= input()
print("Your final result is: "+ love_matching_guess(name_male,name_female))


#A will not overwrite a
a = 4
A = "Sally"
print(a)

#Use Comma can prevent error even with different type string (instead using + )
x = 5
y = "John"
print(x, y)

#THe use of Global function, it will overwrite the variables by order up to down
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
  x = "chicken"
myfunc()

print("Python is " + x)

#so sanh tuoi
age=10
if age<12:
    print("tuoi ti'")
elif age>18:
    print("tre trau")
else:
    print("123456")

#### Rock Paper Scissors Game
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
    
    
