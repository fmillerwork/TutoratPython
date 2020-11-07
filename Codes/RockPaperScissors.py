from random import randint

#players scores
playerScore = 0
botScore = 0

print("\n-----Game Starting-----")
for i in range(5): # 5 rounds
    
    #players choices
    newRoundText = "\nNew round !\n\t-(1) for Rock\n\t-(2) for Paper\n\t-(3) for Scissors\nYour choice : "
    playerChoice = eval(input(newRoundText))

    #pour rendre le programme plus fiable
    while playerChoice != 1 and playerChoice != 2 and playerChoice != 3: #check for input validity (1, 2 or 3)
        playerChoice = int(input("Bad entry... Try something else : "))

    botChoice = randint(1,3)

    #bot choice display
    if botChoice == 3 :
        print("Bot choose to play : Scissors")
    elif botChoice == 2 :
        print("Bot choose to play : Paper")
    else :
        print("Bot choose to play : Rock")

    #round resolution
    if(playerChoice == botChoice):
        print("It's a draw !")
    elif(playerChoice == 1 and botChoice == 2):
        print("Round won by Bot")
        botScore += 1
    elif(playerChoice == 2 and botChoice == 1):
        print("Round won by Player")
        playerScore += 1
    elif(playerChoice == 3 and botChoice == 1):
        print("Round won by Bot")
        botScore += 1
    elif(playerChoice == 1 and botChoice == 3):
        print("Round won by Player")
        playerScore += 1
    elif(playerChoice == 2 and botChoice == 3):
        print("Round won by Bot")
        botScore += 1
    elif(playerChoice == 3 and botChoice == 2):
        print("Round won by Player")
        playerScore += 1
    
    #scores display
    print("Player score :",playerScore,"\nBot score :",botScore)

if playerScore > botScore:
    print("Player won the game !")
elif playerScore < botScore:
    print("Bot won the game !")
else:
    print("It's a draw !")


