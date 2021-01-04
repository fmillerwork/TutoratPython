print("\n-----------More Lists-----------")

print("Quelques fonctions :")
from random import choice 
from random import sample 
from random import shuffle 
L = [1, 5, 8, "coucou", "a", 4, "au revoir"]

print(choice(L))    # Renvoie aléatoirement un élément de la liste L
print(sample(L,3))  # Renvoie aléatoirement n éléments de la liste L (sous la forme d'une liste)
print(L)
shuffle(L) # Mélange les élements de la liste L (ne crée pas de nouvelle liste)
print(L) 

string = "Bonjour, j'aime Python, mais je préfère C#."
L = string.split()  #Découpe le string suivant le caractère entré en paramètre, et renvoie une liste de ces éléments. Le caractère par défaut est le caractère " " (espace)
print(L)
# print(string.split())   Affiche directement la liste renvoyée par la méthode. Ne stocke pas dans une variable.
print(string.split(","))  #Découpe suivant le caractère ",".

L = ["Bonjour,", "j'aime la version", "3", "de Python.", "J'ai 15 en Python."]
print(" ".join(L))  # Inverse de la méthode split(). Renvoie un string composé des éléments de la liste L et chaque éléments est séparé par le caractère " ".


print("List comprehensions (création de listes) :")

from math import sin
string = "Bonjour"
M = ["un", "deux", "trois"]
L0 = [1, 2, 3, 4, 5]

L = [i for i in range(0, 11, 2)]    #Création d'une liste avec uniquement les nombres pairs entre 0 et 11 (exclus)
print(L)

L = ["a" for i in range(10)]    #Elément spécifique. Création d'une liste avec 10 répétition du caractère "a"
print(L)

L = [i**2 for i in range(1, 11)]    #Calcul. Création d'une liste avec le carré des 10 permiers entiers naturels.
print(L)

L = [sin(i) for i in range(1, 11)]    #Calcul de sinus. Création d'une liste avec le sinus des 10 permiers entiers naturels.
print(L)

L = [c*2 for c in string]    #Caractère d'un string. Création d'une liste avec chaque élément qui est une répétition d'un caractère de string.
print(L)

L = [m[1] for m in M]    #Caractère d'une liste de string. Création d'une liste avec chaque élément qui le caractère à l'indice 1 d'un élément de la liste M.
print(L)
#L = [m[2] for m in M]  => string index out of range car M[0] à une longueur de 2 donc m[2] n'existe pas.

L = [i for i in L0 if i % 2 == 0]    #Avec condition if. Création d'une liste L avec les éléments pairs de la liste L0.
print(L)

L = [[i,j] for i in range(1,4) for j in range(1,4)]     #Création d'une liste de liste (liste à 2 dimensions). Chaque élément de la liste principale est une liste de 2 éléments. Ici, c'est l'équivalent d'une matrice 3x3.
print(L)

print([[i,j] for i in range(1,4) for j in range(1,4)])  #On peut directement afficher la liste dans un print sans devoir passer par une variable.


print("Liste à 2 dimensions :")
from pprint import pprint
L = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# L = [[1, 2, 3], 
#      [4, 5, 6], 
#      [7, 8, 9]]

print(L[1][2])  #Affiche l'élément à l'indice 2 dans l'élément (sous liste) à l'indice 1.
print(L)
pprint(L)   #pretty-print => affiche une liste d'une façon plus jolie et compréhensible


