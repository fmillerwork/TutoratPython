dividende = eval(input("\nEntrer le dividende: "))
diviseur = eval(input("Entrer le diviseur: "))
precision = eval(input("Entrer la precision souhaitée: "))

resultat = ""

print("\n",dividende," " * precision ,"|" ,diviseur ,sep="")
print("--------------")

for i in range(1, 9):
    reste = dividende % diviseur
    quotient = int(dividende / diviseur)
    print(" " * (2 + i - len(str(reste))),reste ," " * (precision - i + 1) ,"|" ," " * i ,quotient ,sep="")
    
    resultat += str(quotient)
    if precision > 1 and i == 1:
        resultat += ","
    dividende = dividende % diviseur * 10
print("\nResultat :",resultat)