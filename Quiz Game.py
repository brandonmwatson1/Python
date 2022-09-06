print("Welcome to my quiz!")

playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What is my first name? ")
if answer.lower() == "brandon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What is my last name? ")
if answer.lower() == "watson":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

answer = input("How old am I? ")
if answer.lower() == "29":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " question(s) correct.")
print("You got " + str((score/3) * 100) + "% correct.")

