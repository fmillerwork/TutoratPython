print("---------------- Devoir maison 1 ----------------",end=3*"\n")

# Probleme 1: Division décimale
print("--- Division décimale posée -----------",end=2*"\n")

dividende = eval(input("Entrer le dividende: "))
diviseur = eval(input("Entrer le diviseur: "))
n =  eval(input("Entrer la précision souhaitée: "))

print(dividende/diviseur) # Pour vérifier

# Première ligne: le dividende suivi de suffisamment d'espaces à savoir n
# suivi de | et du diviseur
print( dividende, n*" " + "|", diviseur, sep ="" )

# On calcule la taille des nombres et on trace la ligne horizontale
spDiviv = len( str(dividende) )
spDivis = len( str(diviseur) )
print( (spDiviv+n+1+spDivis) * "-" )

# On réalise successsivement chaque division entière pour la précision souhaitée
for i in range(n):
    quotient = dividende // diviseur
    reste = dividende - quotient * diviseur
    spQuotient = len( str(quotient) )
    spReste = len( str(reste) )
    # Les décallages sont choisis pour garder alignées les unités
    print( (spDiviv-spReste+i)*" ", reste, (n-i)*" " + "|" + (spDiviv+i-spQuotient)*" ", quotient, sep = "" )
    dividende = reste*10 # On "rajoute un zéro"


# Probleme 2: Pierre Feuille Ciseau
print(3*"\n"+"--- Pierre-Feuille-Ciseau -----------",end = 2*"\n")
from random import randint

playerScore = 0 # Initialisation du score joueur
for i in range(5):
    print("Round: ",i+1,"/ 5")
    # Mise à jour joueur
    playerValue = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    # On associe une figure à l'entrée
    if playerValue == 1:
        player = "Rock"
    elif playerValue == 2:
        player = "Paper"
    else:
        player = "Scissors"
    print("You played", player, end = ", ")

    # Mise à jour computer + affichage
    compValue = randint(1,3) # Le tirage est aléatoire
    if compValue == 1:
        computer = "Rock"
    elif compValue == 2:
        computer = "Paper"
    else:
        computer = "Scissors"
    print("computer played", computer+".")

    # Comparaison avec affichage et mise a jour du score
    if compValue == playerValue:
        print ("Draw!")
    # Les score avec une difference modulo 3 de 1 sont gagnants pour le joueur! (alternative au if)
    elif ( playerValue - compValue )%3==1:
        print("You win!")
        playerScore += 1
    else:
        print("You lose!")
        playerScore -= 1
    print()

# Au final le joueur perd si son score est < 0, etc...
if playerScore > 0:
    print("You win the game!")
elif playerScore == 0:
    print("It is a draw!")
else:
    print("You lose the game!")
