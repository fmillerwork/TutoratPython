from math import sqrt

n = eval(input("n = ? "))
isSquareFree = True


for i in range(2,n + 1):
    #si n est divisible par i et sqrt(i) est entier (i est un perfect square)
    if int(n/i) * i == n and int(sqrt(i)) * int(sqrt(i)) == i:
        isSquareFree = False
        print(i, "est un carré parfait : divisible par", int(sqrt(i)) )
        break
    elif int(n/i) * i == n:
        print(i, "n'est pas un carré parfait")
print(isSquareFree)
