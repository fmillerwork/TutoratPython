#Ex 3
'''
weight = float(input("entrer un poids"))
while weight < 0:
    print ("le poids ne doit pas etre negatif")
    weight = float(input("entrer un poids"))
PoidsFinal = 2.20462 * weight
print(PoidsFinal)
'''

#Ex4
password = "polytech"
tries = 5
while True:
    guess = input("Entrer un mdp : ")
    if guess == password:
        print("Connecté !")
        break
    if tries < 2:
        print("Trop tentatives ")
        break
    print("Mauvais Mdp ...")
    tries -= 1

