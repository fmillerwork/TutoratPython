#1

#1

#1.a
#on demamnde à l'utilisateur de rentrer 3 valeurs,que l'on définit ci-dessous:dividende, diviseur et précision souhaitée
dividende=eval(input("entrer un dividende:"))
diviseur=eval(input("entrer un diviseur:"))
precision=eval(input("entrer la précision souhaitée:"))

#1.b
#on affiche les deux premières lignes de la division en utilisant les valeurs définis les lignes d'avant
print(dividende," "*precision,"|",diviseur)
#on utilise les fonctions len() et str() pour ajuster les écarts avec la précision, pour la deuxième
lenght=len(str(dividende))#on définit chaque lenght, ce qui va nous permettre d'avoir le même nombre de - que de valeur définit avant
lenght1=len(str(diviseur))
print("-"*(lenght+precision+4+lenght1))#j'additionne les lenght et la précision et je rajoute 4 pour combler le vide, entre | et le diviseur

#1.C
for i in range (precision): 
    b=dividende//diviseur #je calcule le quotient
    a=dividende-diviseur*b #je calcule le reste de la troisième ligne
    dividende=(a*10)-diviseur #cela correspond aux restes des lignes suivantes, et je mutplie par 10 pour rajouter un O
    print(" "*i,a,((precision+1)-i)*" ","|",(i)*' ',b)

#2
'''
from random import randint #j'utilise la fonction random pour que l'ordinateur choisisse un chiffre au hasard entre 1 et 3
from math import*

ordinateur=randint(1,3)
joueur=eval(input("entrer Pierre,Papier ou Ciseaux:"))#je demande à l'utilisateur de choisir entre pierre papier et ciseaux.
if ordinateur== 1: #Je relies ses valeurs au données, pierre papier et ciseaux. 
    ordinateur= "Pierre"
elif ordinateur== 2:
    ordinateur= "Papier"
else ordinateur==3:
    ordinateur= "Ciseaux"
    

for i in range(5):
    if ordinateur==joueur
               print("egalité") #si l'ordinateur et le joueur font les jeu durant les cinq tours, il y a égalite
    elif ordinateur="Pierre" et joueur="Ciseaux"
                 ordinateur="Ciseaux" et joueur="Papier"
                 ordinateur="Papier" et joueur="Pierre"
               print("l'ordinateur a gagné")
    else ordinateur="Pierre" et joueur="Papier"
                 ordinateur="Ciseaux" et joueur="Pierre"
                 ordinateur="Papier" et joueur="Papier"
                print("le joueur a gagné") 
            
            
            
'''