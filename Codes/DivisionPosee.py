dividende = eval(input("\nEntrer le dividende: "))
diviseur = eval(input("Entrer le diviseur: "))

precision = eval(input("Entrer la précision souhaitée: "))
while precision < 0: #fiabilité du programme (précision toujours positive)
    precision = eval(input("Entrer une précision positive: "))

resultat = ""

print("\n",dividende," " * precision ,"|" ,diviseur ,sep="") #première ligne
print("--------------") #CORRIGER 

for i in range(1, precision + 1):
    reste = dividende % diviseur
    quotient = int(dividende / diviseur)
    print(" " * (2 + i - len(str(reste))),reste ," " * (precision - i + 1) ,"|" ," " * i ,quotient ,sep="") #ligne de division
    resultat += str(quotient) #ajout du quotient de la soustraction dans le résultat
    if precision > 1 and i == 1: #si division demandée donne un quotient global décimal
        resultat += ","
    dividende = dividende % diviseur * 10
print("\nResultat :",resultat)



