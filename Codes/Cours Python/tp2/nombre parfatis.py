diviseurs = []
somme = 0
for n in range (1,10000):
    for i in range (1, n):
        if n%i == 0:
            diviseurs.append(i)
    for i in range(len(diviseurs)):
        somme+= diviseurs[i]
    if  n == somme:
        print("nombre parfait", n)
