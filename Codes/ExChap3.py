from random import random
from random import randint

#Ex2
x = randint(1,50)
y = randint(2,5)
print("x =" ,x ,"y =" ,y , "x**y =",x**y)

#Ex4
#print(round(random()*10, 2))

#Ex5
for i in range(1,50+1):
    print(randint(1,i))
#erreur : range(50) car on commence pas à 0 mais à 1. Il fait donc décaler la borne supérieur du for de 1

#Ex9
hour = int(input("Enter hour (1 to 12): "))
duration = int(input("How many hours ahead ? "))

print("New hour :", (hour + duration) % 12, "o'clock")

#Ex11

kilogrammes = eval(int("kilogrammes : "))
print("pounds =", kilogrammes * 2.2046)

#Ex12

nb = int(input("nombre = "))
factoriel = 1
for i in range(1, nb + 1):
    factoriel *= i
print(factoriel)

#Ex17
#sans IF, compliqué


#Ex18

prix = eval(input("Prix : "))
montantPaye = eval(input("Montant payé : "))
montantRendu = round(montantPaye - prix, 2)
print("Montant à rendre =", montantRendu)

print(int(montantRendu // 20) ,"de 20 €")
montantRendu = montantRendu % 20
print(int(montantRendu // 10) ,"de 10 €")
montantRendu = montantRendu % 10
print(int(montantRendu // 5) ,"de 5 €")
montantRendu = montantRendu % 5
print(int(montantRendu // 2) ,"de 2 €")
montantRendu = montantRendu % 2
print(int(montantRendu // 1),"de 1 €")
montantRendu = montantRendu % 1
print(int(montantRendu // 0.5) ,"de 50 c")
montantRendu = montantRendu % 0.5
print(int(montantRendu // 0.2) ,"de 20 c")
montantRendu = montantRendu % 0.2
print(int(montantRendu // 0.1) ,"de 10 c")
montantRendu = montantRendu % 0.1
print(int(montantRendu // 0.05) ,"de 5 €")
montantRendu = montantRendu % 0.05
print(int(montantRendu // 0.02) ,"de 2 c")
montantRendu = montantRendu % 0.02
print(int(montantRendu // 0.01) ,"de 1 c")
