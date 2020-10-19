from math import log

n = eval(input("valeur de n"))
result = 0
for i in range(1,n+1):
    result += 1/n
print(result - log(n))
