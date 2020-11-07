'''
#Sans résistance inter branches
inverseResEq = 0    #inverse de la résistance équivalente totale

for i in range(1, int(input("Nombre de branches : ")) + 1): # gestion des branches
    resEquivBranche = 0     #res. equiv. dans une branche
    inputStr = "Nombre de résistances dans la branche " + str(i) + " : "     # string pour l'input de la ligne suivante 
    
    for j in range(1, int(input(inputStr)) + 1):     #gestion des résistances dans une branche
        inputStr = "Valeur de la résistance " + str(j) + " : "    # string pour l'input de la ligne suivante 
        resEquivBranche += float(input(inputStr))    #calcul successif de la res. equiv. de la branche 
    
    inverseResEq += 1 / resEquivBranche     #calcul successif de la res. equiv. totale
    
print("Résistance équivalante :", round(1/inverseResEq, 1), "ohm(s)")

'''



#Avec résistances inter branches

resEqTotale = 0    #résistance équivalente totale

for i in range(1, int(input("Nombre de branches avec des résistances : ")) + 1): # gestion des branches
    resEquivBranche = 0     #res. equiv. dans une branche

    inputStr = "Nombre de résistances dans la branche " + str(i) + " : "     # string pour l'input de la ligne suivante 
    for j in range(1, int(input(inputStr)) + 1):     #gestion des résistances dans une branche

        inputStr = "Valeur de la résistance " + str(j) + " : "    # string pour l'input de la ligne suivante 
        resEquivBranche += float(input(inputStr))    #calcul successif de la res. equiv. de la branche 
    print("Résitance équivalente de la branche :", resEquivBranche)
    if i > 1: # on est au moins dans la branche 2
        resEqTotale = resEqTotale * resEquivBranche / (resEqTotale + resEquivBranche)     #calcul de la res. equiv. totale avec la branche courante et la branche equiv précédente
        print("Résitance équivalente totale :", resEqTotale)
        inputStr = "Nombre de résistances entre les branches " + str(i) + " et " + str(i+1) + " : "     # string pour l'input inter branches
        nbResInterBranche = int(input(inputStr))
        if nbResInterBranche > 0:  #les résistances inter branches
            resEquivInterBranche = 0

            for k in range(1, nbResInterBranche + 1):     #gestion des résistances dans l'inter branche
                inputStr = "Valeur de la résistance " + str(k) + " dans l'inter branche " + str(i) + "/" + str(i+1) + " : "    # string pour l'input de la ligne suivante
                resEquivInterBranche += float(input(inputStr))    #calcul successif de la res. equiv. de l'inter branches
            resEqTotale += resEquivInterBranche    #ajout de la res equiv inter branches dans la res equiv totale
            print("Résitance équivalente totale :", resEqTotale)
    else: # pour la première branche, on sauvegarde la res equiv de la branche
        resEqTotale = resEquivBranche
        print("Résitance équivalente totale :", resEqTotale)

print("Résistance équivalante totale :", round(resEqTotale, 1), "ohm(s)")


