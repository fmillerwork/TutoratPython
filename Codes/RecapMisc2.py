print("\n-----------Miscellaneous 2 (divers)-----------")

print("\nConversion :")

decimal = 5.8
print(int(decimal)) #Conversion float => int
print(str(decimal)) #Conversion float => string

entier = 5
print(float(entier)) #Conversion int => float
print(str(entier)) #Conversion int => string

string = 5
liste = [1,2,3]
print(float(string)) #Conversion string => float
print(int(string))  #Conversion string => int
print(str(liste))   #Conversion liste => string

#Liste non exhaustive, cf chapitres précédents

print(list("abcd")) #Conversion string => liste

print("\nRaccourcis :")

#Variables booléennes et conditions

gameOver = True #Variable booleenne
if gameOver == True:
   print('Bye!')

if gameOver:
   print('Bye!')

gameOver = False #Variable booleenne
if gameOver == False:
   print('Bye!')

if gameOver != True:
   print('Bye!')

if not gameOver:
   print('Bye!')

#Opérations
var = 5
var += 10 #Fonctionne aussi avec : /, *, -, %, //, ....
print(var)

#Assignement 
a = b = c = 10
print(a,b,c)

liste = [1,2,3]
a = liste[0]
b = liste[1]
c = liste[2]

a,b,c = liste   #Equivalent aux 3 lignes au dessus

#Conditions
if a==0 and b==0 and c==0:
    print("ok") 
if a==b==c==0:  #Même fonctionnement que le if au dessus
    print("ok")

if 1<a and a<b and b<5:
    print("ok")
if 1<a<b<5: #Même fonctionnement que le if au dessus
    print("ok")


print("\nShort-circuiting :")
words = ["coucou", "au", "écouter"]

#for w in words:
#    if w[4]=='z':   #Va planter pour le mot "au" car il a que 2 caractères donc w[4] n'existe pas
#        print(w)    

for w in words:
    if len(w)>=5 and w[4]=='z':   #Régle le problème en vérifiant la longeur de w. Comme c'est un and, si la première condition est fausse 'len(w)>=5', Python determine que toute la condition est fausse. Il ne poursuit pas le traitement de la condition.
        print(w)


print("\nContinuation :")
#Le caractère \ permet d'écrire une condition sur plusieurs lignes
string = "bonjour"
if 'a' in string or 'b' in string or 'c' in string \
    or 'd' in string or 'e' in string:  
    print("ok")


print("\nFormating :")

#Utilisation des conversions pour pouvoir utiliser les formattages avec d'autres types. 

#Float
a = 23.60 * .25
print('The tip is {:.2f}'.format(a))    #Formate avec 2 décimales après le "."
print('The tip is {:8.2f}'.format(a))    #Idem au dessus et fait en sorte de décaler le nombre de 8 cases vers la droite.

#Integer
print('{:3d}'.format(2))    #Fait en sorte de décaler le nombre de 3 cases vers la droite.
print('{:3d}'.format(25))
print('{:3d}'.format(138))

print('{:^5d}'.format(2))   #Fait en sorte de centrer le nombre sur 5 cases
print('{:^5d}'.format(222))
print('{:^5d}'.format(13834))

print('{:,d}'.format(1000000))  #Place des virgules pour avoir un entier à l'américaine

#String
print('{:^10s}'.format('Hi'))   #Centre le string sur 10 cases
print('{:^10s}'.format('there!'))

print('{:>6s}'.format('Hi'))    #Fait en sorte de décaler le string de 6 cases vers la droite.
print('{:>6s}'.format('There'))

