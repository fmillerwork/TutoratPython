#Ex4

L = eval(input("Entrer une liste contenant des nombre entre 1 et 12 : "))
for i in range(len(L)):
    if L[i] > 10:
        L[i] = 10
print(L)


#Ex7
L = eval(input("Entrer une première liste : "))
M = eval(input("Entrer une seconde liste de la même taille que la première : "))

if len(M) != len(L):
    print("Veuillez recommencer le programme....")
else:
    N = []
    for i in range(len(L)): #ou len(M)
        N.append(L[i] + M[i])
    print(N)


#Ex10
L = [1,2,3,4,5,6,7,8,9] #on peut demander une liste à l'utilisateur
lastElement = L[-1] #L[8] ici. On utilise un variable de swap.

for i in range(len(L)-1, 0, -1): #de l'indice 8 à 1 ici
    L[i] = L[i-1]
L[0] = lastElement
print(L)
