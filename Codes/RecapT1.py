#Ceci est une ligne de commentaire
'''
Ceci sont 
plusieurs
lignes de commentaires
'''

#Écrire des informations dans la console
'''
print("\n-----------print()-----------")
print("Coucou !") #Affichage simple
print("Coucou", "les", "amis !") #Affichage multiple
nbAmis = 5
print("Coucou mes", nbAmis + 2, "amis !") #Affichage de valeurs de variables + calcul
print("a", "e", "i", "o", "u", "y", sep= 2*"|") #argument sep (séparateur) | par défaut => sep=" "
print("Bonjour !", end=" ") #argument end ('finiseur' ) | par défaut => end="\n"
print("Comment vas-tu ?")
coucouStr = "Coucou \n"
print(coucouStr, "\t Ceci est une tabulation / indentation") #Caractères spéciaux : retour à la ligne => \n et tabulation => \t
'''

#Demander et enregistrer des données de l'utilisateur
'''
print("\n-----------input()-----------")
a = eval(input("Entre un int : "))
print("eval(input())", a, "Type :", type(a)) #<class 'int'> car eval() converti le string donné par input() en int
a = eval(input("\nEntre un float :\n"))
print("eval(input())", a, "Type :", type(a)) #<class 'float'> car eval() converti le string donné par input() en float
a = eval(input("\nEntre quelque chose (lettres et/ou nombres) avec \"\":\n"))
print("eval(input())", a, "Type :", type(a)) #<class 'str'> car on a explicitement dit que c'est un string avec les ""
a = input("\nEntre quelque chose (lettres et/ou nombres) sans \"\":\n")
print("input()", a, "Type :", type(a)) #<class 'str'> car input() seul donne toujours un string
a = input("\nEntre quelque chose (lettres et/ou nombres) avec \"\":\n")
print("input()", a, "Type :", type(a)) #<class 'str'> car input() seul donne toujours un string

a = int(input("\nEntre un float : \n"))
print("int(input())", a, "Type :", type(a)) #<class 'int'> car int() converti le string donné par input() en int
a = float(input("\nEntre un int : \n"))
print("float(input())", a, "Type :", type(a)) #<class 'float'> car float() converti le string donné par input() en float
#ATTENTION ! Écrire str(input()) est inutile car input() donne déjà un string.
'''
#Utilisation de input() directement dans un if, for, while, etc. Permet de de réduire le nombre de lignes.
'''
if int(input("Nb = ")) > 0:
    print("Nb est positif")
else :
    print("Nb est négatif")
'''

#Variables
'''
print("\n-----------Variables-----------")
a = 5 #déclaration (on lui donne un nom) et initialisation (on lui donne une valeur) de la variable a
print("Convention de nommage des variables (En utiliser une à la fois, ne pas faire de mélange. Jamais d'accents !!)")
print("\tCamel Case :", "Première lettre de chaque mot en maj sauf pour le premier mot.", "Ex : maVariable, resteDivision")
print("\tPascal Case :", "Première lettre de chaque mot en maj.", "Ex : MaVariable, ResteDivision")
print("\tSnake Case :", "Chaque mot est séparé par un _ .", "Ex : ma_variable, reste_division")



print("\nCalculs :")
a = 11
b = 5
c = a // b
print("Division entière",a ,"//" ,b ,"=" , c)
print("Division entière",a ,"//" ,b ,"=" , a // b) #plus pratique et préférable dans certains cas pour réduire le nombre de lignes
print("Reste division",a ,"%" ,b ,"=" , a % b)

#Raccourcis d'écriture pour les calculs

print("\nRaccourcis d'écriture :")
a = 11
aSave = a #sauvegarde de la valeur de a dans aSave pour pouvoir afficher cette valeur après le calcul
a += b # => a = a + b
print("a = 11  => ", "a +=", b," =>  a =" , a)
a = 11
a -= b  # => a = a - b
print("a = 11  => ", "a -=", b," =>  a =" , a)
a = 11
a *= b # => a = a * b
print("a = 11  => ", "a *=", b," =>  a =" , a)
a = 11
a /= b # => a = a / b
print("a = 11  => ", "a /=", b," =>  a =" , a)
a = 11
a //= b # => a = a // b
print("a = 11  => ", "a //=", b," =>  a =" , a)
a = 11
a %= b # => a = a % b
print("a = 11  => ", "a %=", b," =>  a =" , a)
'''
'''
print("\nConversions :")
a = 5 # int
print(a, "Type :", type(a))
b = float(a) #float
print(b, "Type :", type(b))
c = str(a) #string (str)
print(c, "Type :", type(c))
'''
'''
print("\n-----------for-----------")
print("for i in range(5)")
for i in range(5): #5 itérations de i, début à 0 et fin à 4
    print(i)
print("\nfor i in range(1, 6)")
for i in range(1, 6): #5 itérations de i, début à 1 et fin à 5
    print(i)
print("Indentation :")

for i in range(5): #5 itérations de i, début à 0 et fin à 4
    print("Itération n° ", end="")
    print(i)
print("Fin du for")

'''


    