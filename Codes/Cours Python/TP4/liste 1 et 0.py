#l = [i**2 for i in range(1000)]  rempli avec le carré des 1000 premiers entiers

l = [[1] + [0]*i for i in range(10)]
print(l)

print("")

l = [y for i in range(8) for y in [1] + [0]*i]
print (l)
