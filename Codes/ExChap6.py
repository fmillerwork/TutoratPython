#Ex3

    #Version classique
formule = input("Entrer une formule : ")
nbParOuvertes = formule.count("(")
nbParFermees = formule.count(")")
if  nbParOuvertes == nbParFermees :
    print("Il y a autant de de parenthèses ouvertes que de parenthèses fermées.")
else:
    print("Il manque",nbParOuvertes - nbParFermees, "parenthèse(s) fermée(s)")


    #Version compacte
formule = input("Entrer une formule : ")
if formule.count("(") == formule.count(")"):
    print("Il y a autant de de parenthèses ouvertes que de parenthèses fermées.")
else:
    print("Il manque",formule.count("(") - formule.count(")"), "parenthèse(s) fermée(s)")
    

#Ex6

s = input("Entrer un string :")
print(s)
s = s.lower()
s = s.replace(".","")
s = s.replace(",","")
print(s)



#Ex7

    #Première version
mot = input("Entrer un mot : ")

if mot == mot[::-1]:
    print(mot, "est un palindrome !")
else:
    print(mot, "n'est pas un palindrome !")

    #Compacte
mot = input("Entrer un mot : ")
print(mot, "est un palindrome ?" ,mot == mot[::-1]) #mot == mot[::-1] donne un booléen













#Ex19
'''
largeNumber = input("Enter un grand nombre entier : ")
conventionNumber = ""
for i in range(1 , len(largeNumber) + 1, 3):
    if i != 1: #pour ne pas mettre de virgule au début du nombre mais après une série de 3 chiffres
        conventionNumber += ","
    conventionNumber += largeNumber[-i:-(i+3):-1] #conventionNumber est concaténé avec les caractères -i à -(i+2) de largeNumber car -(i+3) est exclus
print(largeNumber) #modèle
print(conventionNumber[::-1]) #inversion du string
'''