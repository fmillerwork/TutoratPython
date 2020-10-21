n = eval(input("Somme à exprimer "))
print("50 :",n//50) #résultat entier d'une divisions
n-=n//50*50
print("20 :",n//20)
n-=n//20*20
print("10 :",n//10)
n-=n//10*10
print("2 :",n//2)
n-=n//2*2
print("1 :",n//1)
