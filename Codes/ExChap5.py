#Exo 4 (2 variantes)

#10 lignes
'''
sum = 0
sign = True # False => soustraction, True => addition
for i in range(1,2001):
    if sign : #si sign = True
        sum += i
        sign = False
    else: #si sign = False
        sum -= i
        sign = True
print(sum)

#6 lignes
sum = 0
coef = 1
for i in range(1,2001):
    sum += coef*i
    coef *= -1 #inversion du signe   => coef = coef * -1
print(sum)
'''
#Exo 5
'''
nb = int(input("Nb = "))
divisorSum = 0 #camelCase
for i in range(1, nb + 1):
    if nb % i == 0:
        print(i, "is a divisor")
        divisorSum += i
print("Divisors sum =", divisorSum)
'''
#Exo 13
'''
from random import randint
score = 0
for i in range(10):
    nb1 = randint(1,9)
    nb2 = randint(1,9)
    print("Question 1:", nb1, "x",nb2 , "=", end=" ")
    if int(input("")) == nb1 * nb2:
        print("Rigth !")
        score += 1
    else : 
        print("Wrong. The answer is ", nb1 * nb2)
if score < 3:
    print("Score =", score, "/10") #ajouter des if et des print différents en fonction du score
'''