print("\n-----------Listes numériques-----------")

print("Intro :")
'''
liste = [1, 2, 3] # déclaration et initialisation d'une liste (avec ou sans espaces)
listeVide = [] # liste vide

#liste sur plusieurs lignes (pour les longues listes ou pour structurer le code)
longueListe = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
print(liste[1]) #affichage de l'élément à l'indice 1

listeInput = eval(input("Entrer une liste [..., ..., ...] :"))
print(listeInput)
# raccourcis d'écriture : print(eval(input("Entrer une liste :")))
'''
'''
print("Ressemblances avec les string :")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(liste), "\n") # len(liste)

if 1 in liste: # opérateur in
    print("1 est contenu dans la liste")
if 5 in liste: 
    print("5 est contenu dans la liste\n")

#idem pour les méthodes liste.index(x) et liste.count(x)
#idem pour l'indexation (liste[1], liste[-5]) et le partitionnement (liste[1:5], liste[5:])
#idem pour les opérateurs + (concaténation) et * (répétition)

for i in liste: #boucle calculant le carré de chaque élément de la liste
    print(liste[i] * liste[i]) 

'''
print("Fonctions pour les listes :")
liste = [5, 2, 9, 7, 1, 6, 4, 8, 3]

# len(liste) cf plus haut et string
print("Somme :", sum(liste)) # sum => somme tous les éléments de la liste
print("Minimum :", min(liste)) # min => renvoie le minimum de la liste
print("Maximum :", max(liste)) # max => renvoie le maximum de la liste

liste.append(0) #ajoute l'élément 0 à la fin de la liste
print(liste)
liste.append([-1, -2]) #ajoute la liste [-1, -2] à la fin de liste. [-1, -2] est un élément unique. Il s'agit d'une liste contenu dans une liste.
print(liste)

del liste[-1] #supprime le dernier élément de la liste.
print(liste)

liste.sort(reverse=True) #tri la liste dans l'ordre décroissant
print(liste)

liste.sort() #tri la liste dans l'ordre croissant
print(liste)

liste.reverse() #inverse la liste
print(liste)

liste.remove(0) #supprime la première occurence de 0 dans la liste
print(liste)

print(liste.pop(0)) #supprime l'élément à l'indice 0 et retourne la valeur de cet élément
print(liste)

liste.insert(5,9) #insère l'élément 9 à l'indice 5. Les éléments déjà présents à l'indice 5 et plus, sont décalés vers la droite de 1.
print(liste)

