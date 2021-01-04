# 1.Division
#nommage + répétition (string) + égalité dans exo 2

print('Exo 1')
num = eval(input('Entrer le dividende: ')) # on demande à l'utilisateur  
num2 = eval(input('Entrer le diviseur: ')) # d'entrer les élements pour la division 
num3 = eval(input('Entrer la précision: '))
print(num, num2, sep='      |')
print(10*'-')
print(num-num2*(num//num2), num//num2, sep='      |')#on définie à quoi correspond le dividende et le reste
div = num-num2*(num//num2)
di = div*10
for i in range(num3-1) :                      
    div = di-num2*(di//num2)                   # on définie la nouvelle valeur du dividende
    print(di-num2*(di//num2), di//num2)
    di = div*10           #on met à jour le dividende pour passer à la ligne suivante
    
# 2.Pierre-Feuille-Ciseaux
print('Exo 2')
from random import *
print("Sachant que 1=pierre, 2=feuille, 3= ciseaux, entrer un nombre entre 1 et 3")
count = 0
for i in range(5) :
    num = eval(input("entrer un nombre entre 1 et 3: ")) #On demande au joeur d'entrer un nombre entre 1 et 3 qui correspond à pierre, feuille ou ciseaux
    if num == 1:
        joueur = "pierre"
    elif num == 2:
        joueur = "feuille"
    elif num == 3:
        joueur = "ciseaux"
    n = randint(1,3)                   #On demande à l'ordinateur de choir un nombre entre 1 et 3 qui correspond à pierre, feuille ou ciseaux
    if n == 1:
        ordi = "pierre"
    elif n == 2:
        ordi = "feuille"
    elif n == 3:
        ordi = "ciseaux"
    print("Vous :", joueur, "Ordinateur :", ordi,end=' : ')
    if num == 1 and n == 3:
        print("Vous avez gagne.")                    #On note toutes les possibilités pour lesquels on gagne, perd ou fait égalité et on affiche le résultat tour par tour
        count = count + 1                            #On met en place un système de comptage afin de déterminer le gagnant à la fin des 5 manches
    elif num == 1 and n == 2:
        print("Vous avez perdu.")
        count = count - 1
    elif num == 1 and n == 1:
        print("Egalite.")
        count = count  
    if num == 2 and n == 1:
        print("Vous avez gagne.")
        count = count + 1
    elif num == 2 and n == 3:
        print("Vous avez perdu.")
        count = count - 1
    elif num == 2 and n == 2:
        print("Egalite.")
        count = count 
    if num == 3 and n == 2:
        print("Vous avez gagne.")
        count = count + 1
    elif num == 3 and n == 1:
        print("Vous avez perdu.")
        count = count - 1
    elif num == 3 and n == 3:
        print("Egalite.")
        count = count
if count == 0:
    print("Vous avez fait égalité dans ce match en 5 manches")     #On détermine le gagnant en fonction du nombre de points et on affiche le gagnant 
elif count < 0:
    print("Vous avez perdu dans ce match en 5 manches")
elif count > 0:
    print("Vous avez gagné dans ce match en 5 manches")
