name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
   
    answer = input("You come to a river. You can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an croc!")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lost the game!")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You have come to a bridge that looks sketchy. Do you want to walk across it or go back (back/cross)? ").lower()

    if answer == "back":
        print("You go back and you lose! ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the starnger and they are mad at you. You lose!")
        else: 
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")

print("Thank you for trying", name + "!")