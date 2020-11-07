print("\n-----------String (chaîne de caractères)-----------")
'''
print("\nIntro :")
#un string ou chaîne de caractères est un ensemble de caractères ("a", "(", "%", "4") => CF caractères ASCII

Astring = "1000" #string
Astring = '1000' #string    possible d'utiliser "" ou '' pour ouvrir le string et utiliser l'autre symbole comme caractère du string
Aint = 1000 #int

stringMultilignes = """ Coucou, ceci est un 
string sur plusieurs lignes """  # string sur plusieurs lignes => à n'utiliser que lors que string est très long

stringEval = eval(input("Entrer un string : "))
stringNoEval = input("Entrer un string : ")
#les 2 lignes sont équivalentes (si on souhaite entrer une donnée de type string) car input renvoie déjà un string.
#Si on rentre une donnée de type int, float, etc. sans "", cette équivalence n'est plus valide => CF Tuto 1 avec input()

chaineVide = "" #string vide

a = "bonjour"
print(len(a)) #affiche la longueur du string a (nombres de caractères)

'''
'''
print("Concaténation et répétition :")

#concaténation
a = "abc"
b = "def"
print(a + b)
c = "abc" + "def" 
print(a + b)

#peut être utiliser pour construire des string au fur et à mesure d'un programme
# (DM1) la variable resultat est construite au fur et à mesure de l'écriture de la division posée

dividende = eval(input("\nEntrer le dividende: "))
diviseur = eval(input("Entrer le diviseur: "))
precision = eval(input("Entrer la précision souhaitée: "))

resultat = ""

#Affichage des 2 premières lignes ....

for i in range(1, precision + 1):
    #calculs et affichages ....
    
    resultat += str(quotient) #ajout du quotient de la soustraction dans le résultat
    if precision > 1 and i == 1: #si division demandée donne un quotient global (final) décimal
        resultat += ","
    
    dividende = dividende % diviseur * 10
print("\nResultat :",resultat)


#répétition
a = "a" * 4
print(a)

'''
'''
print("Opérateur in :")
string = "bonjour"

#Dans les if
if "a" in string: #vérifie chaque caractère du string à la recherche de "a". La condition est True si string contient "a" 
    print("le caractère 'a' est contenu dans le string")
elif "j" in string: #idem mais avec "j"
    print("le caractère 'j' est contenu dans le string")
'''
'''
print("Indexation (indexing):")
string = "Hello world !"

print(string[0]) #affiche le premier caractère de la variable string
print(string[1]) #affiche le second caractère 
print(string[-1]) #affiche le dernier caractère 
print(string[-2]) #affiche l'avant dernier caractère. Ici, c'est le caractère " " (espace)
# Le comptage débute à partir de 0 et non de 1.
#Si l'indice est négatif, cela compte depuis la fin.

#Si l'indice dépasse la taille du string, le programme plante => IndexError : string index out of range
#print(string[20])
'''
'''
print("Partitionner (slice):")
string = "bonjour à tous !"

#string[ :5] et string[:5] sont équivalents
print("string[2:5]   ",string[2:5]) #affiche les caratères aux indices 2, 3 et 4. Comme avec range(x) ou range(y,x), x est exlus (borne supérieur)
print("string[ :5]   ",string[:5]) #affiche les 5 premiers caractères (0, 1, 2, 3, 4) (5 exclus)
print("string[5: ]   ",string[5:]) #affiche tous les caractères à partir de l'indice 5 (inclus)
print("string[-2: ]   ",string[-2:]) #affiche les 2 dernier caractères
print("string[ : ]   ",string[:]) #affiche toute la chaîne
print("string[1:7:2]   ",string[1:7:2]) #affiche des indices 1 à 6 (7 est exclu) avec un pas de 2
print("string[ : :-1]   ",string[::-1]) #affiche la chaine dans le sens inverse
print("string[ : :-2]   ",string[::-2]) #affiche la chaine dans le sens inverse avec un pas de 2
'''
'''
print("Changer les caractères d'un string :")
#Dans l'absolu, c'est impossible.
#Obligation de reconstruire un string en opérant les modif désirées.
s1 = "coucou"
s2 = s1[:3] + s1[4:] #en copie tous les caractères de s1 dans s2 sauf le second 'c'
print(s1,s2,sep='\n')
'''
'''
print("Dans les for (looping) :")

string = "bonjour"
for i in range(len(string)): #boucle for utilisant la longueur du string
    print(string[i])
'''
'''
print("Fonctions sur les string :")
#Definition : retourne => fournit la valeur

#x.lower()  => renvoie une nouvelle chaine dans tous les de x sont en mininuscules
string = "COUCOU"
print(string.lower())
print(string,"\n")

#x.lower()  => renvoie une nouvelle chaine dans tous les de x sont en majuscules
string = "coucou"
print(string.upper())
print(string,"\n")

#x.replace(a,b)  => renvoie une nouvelle chaine dont les occurences a sont remplacées par b. a et b sont des string (1 ou plusieurs caractères).
print(string.replace("co", "ki"))
print(string,"\n")

#x.count(a) => compte le combre d'occurences de a (a est un string) dans le string x
print("Nombre de 'o' dans 'coucou' :", string.count("o"), end="\n\n")

#x.index(a) => retourne l'indice de la première occurence de a dans x. a est un string.
print("Première occurence de 'u' dans coucou à l'indice :", string.index('u'), end="\n\n")

#x.isalpha() => renvoie True si tous les caractères de x sont les lettres
if string.isalpha():
    print("La variable contient que des lettres")
else:
    print("La variable ne contient pas que des lettres")
'''
'''
print("Caractère d'échappement :")
#le caractère '\' permet de changer le fonction de certains autres caractères.

print("Hello\nworld !") # \n => retour à la ligne
print("\tHello world !") # \t => tabulation
print("\"Hello world !\"") # \"" => permet d'écrire un " dans un string sans mettre fin à ce dernier (lorsqu'on utilise "" pour définir le string). Idem avec '
print("Hello\\world ! ") # \\ => permet d'écrire '\' dans un string sans qu'il n'y ai d'ambiguiter
print("Hello\world ! ") # ambiguité dans ce cas. Certains IDE le signale.
'''

