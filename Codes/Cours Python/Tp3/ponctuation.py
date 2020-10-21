from string import punctuation #importation ponctuation

txt = input("Ecrire un texte : ")
mot = 1
iteration = 0
ponctuation = 0

#1
for i in txt:
    if i == " ":
        mot +=1
print ("Nombre de mots :", mot)

#2
#\" pour écrire " dans un string
punctuation
print("Itération de \"frite\" :", txt.count("frite"))

#3
for i in punctuation:
    for j in txt:
        if i == j:
            ponctuation += 1
print("Itération de ponctuation :", ponctuation)

#4
txt2=txt
for j in txt:
    for i in punctuation:
        if i == j:
            txt2=txt2.replace(j,"")
print (txt2)

#5
print(txt2.lower())

#6
print(txt.replace(txt[0], txt[0].upper()))
