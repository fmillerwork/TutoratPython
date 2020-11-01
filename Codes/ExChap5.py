#Exo 4
#10 lignes
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

#Exo 13
