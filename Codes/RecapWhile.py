print("\n-----------While-----------")

print("Intro :")

nom = input("Entrer un nom de famille : ")
while not nom.isalpha():
    nom = input("Entrer un nom de famille : ")

print("Utilisations :")

#Vérification des données entrées en input
#Répéter une action jusqu'à ce que l'utilisateur décide de quitter
#Simuler un for
#Répeter une action pour un nombre de fois inconnu (on utilise le for pour répéter une action un nombre de fois connu)
#....

print("Boucle infinie :")
#La boucle se répète à l'infinie et souvent l'IDE bug....
#Y faire attention
#S'utilise que dans certains cas spécifiques.

#i = 5
#while i < 6:   => la condition i < 6 est toujours true
#   print("coucou")

#while True:
#    print("Coucou")


print("Instruction break :")

#S'utilise avec les while et les for. Permet de mettre fin à la boucle. L'itération en cours ne se termine pas.
from random import randint

for i in range(10):
    num = eval(input("Entrer un nombre (-1 pour quitter) : "))
    if num == -1:
        print("Vous avez quitté")
        break


print("Deviner le nombre (entre 1 et 10)")
reponse = randint(0,10)
while True:
    essai = int(input("Faites un essai : "))
    if essai == reponse:
        print("Bravo !")
        break

print("Structure Do While :")

# Dans l'exemple précédent, il s'agit d'un équivalent d'un structure Do While.
# Do While en java :
# do{
#   ......
#   ......
# }while(condition);
# 
# Le programme exécute toujours au moins une itération avant de vérifier la condition dans le while. Cette condition est une condition de répétition !
#
#
# Equivalent d'un Do While en Python :
# while True:
#   .....
#   .....
#   if(condition){
#       break
#   }
#
# Comme la contition du while est True, le programme exécute toujours au moins une itération avant de tester la condition de répétition (celle du if).
# Si elle est vérifiée, la boucle d'arrète. C'est donc une contition d'arrêt et non plus une condition de répétition !

print("Instruction else :")

# Avec les for
for i in range(10):
    num = eval(input("Entrer un nombre (-1 pour quitter) : "))
    if num == -1:
        print("Vous avez quitté")
        break
else:   #S'exécute si et seulement si la boucle précédente n'a pas été interrompue par un break.
    print("Vous n'avez pas quitté la boucle !")

# Au final, le break et le else permettent de réaliser certains actions avec moins de lignes de code.