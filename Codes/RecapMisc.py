print("\n-----------Miscellaneous (divers)-----------")

print("\nCompteur et somme :")
count = 0 #déclarer le compteur avant le for. S'il est déclaré dans le for, il se reset à 0 à chaque itération.
for i in range(10):
    if i % 2 == 0: # si i est pair
        count += 1
        print(i)
print("Il y a",count , "nombres pairs")

print("\nSwapping (échange de valeurs) :")
a = 5
b = 10

a = b # a = b et b = 10 donc a = 10 (valeur de a est perdue)
b = a # b = a mais a = 10 donc b reste à 10
print("a =", a, "et b =", b)

a = 5
b = 10

temp = a #on stocke la valeur de a dans la variable temp (temporaire)
a = b 
b = temp
print("a =", a, "et b =", b)

print("\nFlag variable (variable 'indicative') :")

contains = False #fonctionne très bien avec des int, str ou float mais plus instinctif avec des booléen

for i in range(10):
    if i == 5:
        contains = True
if contains: # if contains == True
    print("Contient 5 !")
else:
    print("Ne contient pas 5 !")
#Il existe de bien meilleurs méthodes pour cette application mais c'est pour l'exemple.

print("\nMaxi et Mini :")

maxi = 0
mini = 0
for i in range(5):
    nb = eval(input("Nb à comparer = "))
    if nb < mini:
        mini = nb
    elif nb > maxi: #un if fonctionne aussi ici car les conditions du if et du elif sont liées (si la première condition est Vraie, la seconde est obligatoirement fausse et inversement).
        maxi = nb
print("Maxi =", maxi, "et Mini =", mini)

print("\nDébogage :")
    #Tester les lignes individuellement sur le Shell lors que celà est possible (Ex : lignes qui utilisent des variables nécessite d'être adaptées)
    #Insertion de print() pour "suivre" le déroulement du programme et voir dans quelles boucles et if il rentre.
