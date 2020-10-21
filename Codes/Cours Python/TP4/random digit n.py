from random import *
# function(n, a=2):   ici, on met pas défaut a = 2 mais on peut
#la changer lors de l'utilisation de la fonction

def randomN(n):
    string = ""
    for i in range(n):
        string = string + str(randint(1,9))
    print (string)  

randomN(int(input("Entre un nb ")))
