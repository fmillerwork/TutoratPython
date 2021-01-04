print("\n-----------Functions (fonction)-----------")

print("\nIntro :")

def printHello():   #Définition de la fonction printHello(). Attention aux parenthèses !!
    print("hello !")

printHello()    #Appel de la fonction printHello()

def dessinerCarre():  #Définition de la fonction dessinerCarre().
    print('*' * 15)
    print('*', ' '*11, '*')
    print('*', ' '*11, '*')
    print('*' * 15)

dessinerCarre() #Appel de la fonction dessinerCarre()

print("\nArguments / parameters (arguments et paramètres):")

def printATimesHello(n):    #Argument n
    print("Hello " * n)

printATimesHello(5) #Appel de la fonction printATimesHello(n) avec n = 5
printATimesHello(2) #Appel de la fonction printATimesHello(n) avec n = 2

times = 3
printATimesHello(times) #Appel de la fonction printATimesHello(n) avec n = 3

def multiplePrint(string, n):   #Fonction à plusieurs arguments. Utiliser des noms explicites pour les arguments
    print(string * n)

multiplePrint("Coucou", 2)


print("\nReturn values (retourner des valeurs) :")
# Il est possible de retourner n'importe quel type de valeur avec une fonction (liste, int, bool, float, string, ...)
def convert(celsiusTemp): #Définition de la fonction convert(t) qui retourne l'équivalent en Fahrenheit de la température en argument.
    return celsiusTemp*9/5+32   #Renvoie la valeur de 'celsiusTemp*9/5+32' suite à l'appel de la fonction
    
print(convert(20))

#Attention ! Une fonction qui retourne une valeur s'arrète dès que le return est exécuté.
#def convert2(celsiusTemp): 
#    return celsiusTemp*9/5+32
#    print("coucou")    #Problème ici....


print("\nDefault arguments and keyword arguments (Arguments par défaut et arguments mot-clé :")

#Argument par défaut.
#Les arguments par défaut doivent être déclarés après les arguments classiques.
def multiplePrint2(string, n=1): # n = 1 par défaut (si on ne spécifie pas de valeur pour n)
    print(string * n)
    print() 

multiplePrint2('Hello', 5)
multiplePrint2('Hello') #utilisation de la valeur par défaut de n.

#Argument mot-clé.
#Les arguments mot-clé sont utilisés pour bien differencier les arguments lors des appels.
#Utile lorsqu'on a plusieurs arguments de même type où qu'on veut gagner en lisibilité lors des appels.
def fancyPrint(text, color='black', background='white',
        style='normal', justify='left'):
    print("bla bla bla")

fancyPrint('Hi', style='bold')   #Les arguments mot-clé permettent de dire à python à quel argument on donne la valeur.
fancyPrint('Hi', color='yellow', background='black')
fancyPrint('Hi')


print("\nVariables locales :")

#Les variables locales sont propres à la fonction dans laquel elle sont déclarées
def func1():
    for i in range(10):
        print(i)

def func2():
    i=100
    func1()
    print(i) #Affiche la valeur de la variable i de la fonction func2()


print("\nVariables globales :")
#Les variables globales peuvent être modifier dans plusieurs fonctions.

def reset():
    global timeLeft #En dit que la variable timeLeft est la variable global et non une nouvelle variable locale de la fonction.
    timeLeft = 0
    
def printTime():
    print(timeLeft)    #Ici, la fonction va prendre la valeur de timeLeft qui est en dehors de la fonction.

#print_time()   #Problème ici => la variable timeLeft n'est toujours pas déclarée => crash du programme
timeLeft=30
printTime()
reset()
printTime()



#   Prochaine étape => POO (Programmation orientée objet)