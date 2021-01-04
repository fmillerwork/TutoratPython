print("\n-----------Text files (fichiers texte)-----------")

print("\nLecture :")

linesFile1 = [line.strip() for line in open('textFile.txt')]
linesFile2 = [line.strip() for line in open('dossier/textFile2.txt')]

print(linesFile1)
print(linesFile2)

stringFile1 = open('textFile.txt').read()
print(stringFile1)

print("\nType des chemins :")

#Chemin relatif
#Chemin écrit à partir de la localisation du fichier actuel.
#Exemple : "dossier/textFile2.txt" et "textFile.txt"
#Dans le second exemple, le fichier textFile.txt est dans le même dossier que le fichier Python.
# .txt, .py sont les extensions des fichiers. Ce sont respectivement des fichiers texte et des fichiers python. 

#Chemin absolu
#Chemin écrit à partir de la racine d'un système de stockage.
#Exemple : "S:\Bureau\TutoratPython\Codes\dossier"


print("\nEcriture :")

f = open('textFile.txt', 'w') #Ouverture du fichier et on lui associe un objet f. On indique qu'on souhaite l'ouvrir en écriture => "w"
print('This is line 1.', file=f)    #Ecriture dans le fichier f
print('This is line 2.', file=f)
f.close()   #Fermeture du fichier f.

