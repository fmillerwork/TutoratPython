#Ex3
'''
kilo = float(input("Kilogrammes : "))

while(kilo < 0 ):
    kilo = float(input("Kilogrammes : "))
print("Pounds = ", 2.20462 * kilo)
'''

#Ex4
'''
password = "polytech"
tries = 5
for i in range(5):
    guess = input("Entrer un mot de passe : ")
    if(guess == password):
        print("Vous êtes identifié")
        break
    print("Mauvais mot de passe") # idem que si on le mets dans un else
else :
    print("Vous avez utilisé vos 5 tentatives....")
'''


#Ex19
'''
from random import randint, choice
from pprint import pprint
L = []

for ligne in range(9):  #ligne
    subL = []
    if ligne == 0:    #Première ligne
        for col in range(9):  #Colonnes
            nb = randint(1,9)
            while subL.count(nb) != 0: #(Condition du Do While) est présent dans la ligne et est présent dans la colonne
                nb = randint(1,9)
            subL.append(nb)
        L.append(subL)
        pprint(L)
    else: # Autres lignes
        for col in range(9): # Colonnes
            #Valeurs possibles en fonction des colonnes
            possibleValues = [i for i in range(1,10)]
            for l in range(ligne):
                possibleValues.remove(L[l][col])
            nb = choice(possibleValues)
            print(nb)
            a = input("Avant while : ")
            while subL.count(nb) != 0: #(Condition du Do While) est présent dans la ligne et est présent dans la colonne
                nb = choice(possibleValues)
                print(nb)
                a = input("Dans while : ")
            subL.append(nb)
            print(subL)
        L.append(subL)
        pprint(L)
pprint(L)
'''



'''
for ligne in range(9):  #ligne
    subL = []
    if ligne == 0:    #Première ligne
        for col in range(9):  #Colonnes
            nb = randint(1,9)
            while subL.count(nb) != 0: #(Condition du Do While) est présent dans la ligne et est présent dans la colonne
                nb = randint(1,9)
            subL.append(nb)
        L.append(subL)
    else: # Autres lignes
        for col in range(9): # Colonnes
            while True:   # Do While 
                isPresentInCol = False
                nb = randint(1,9)
                for i in range(len(L)): #Vérification de chaque ligne
                    if L[i][col] == nb: # Même chiffre dans une ligne supérieure, même colonne
                        isPresentInCol = True
                        break 
                if subL.count(nb) == 0 and not isPresentInCol : #(Condition d'arrêt du Do While) n'est pas présent dans la même ligne et n'est pas présent dans la même colonne
                    break
            
            subL.append(nb)
        L.append(subL) 
pprint(L)
'''