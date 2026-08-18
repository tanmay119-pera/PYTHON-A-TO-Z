'''                                        GUESS THE NUMBER                                                        '''

import random 

target=random.randint(1, 100)

while True:
    userChoice = input("Guess the target or quit(Q):")
    if (userChoice =="Q"):
        break 
    
    userChoice = int(input("guess the number : "))
    if(userChoice == target):
        print("success : correct number!")
        break
    elif(userChoice<target):
        print("your number was to small to guess,Take a bigger guess..")
    else:
        print("your number was to big to guess, Take a smaller guess")

              
print("-----------GAME OVER---------------")