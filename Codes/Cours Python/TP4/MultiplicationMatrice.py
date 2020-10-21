taille = int(input("Matix size")
m1 = input("Matrice 1 :")
m2 = input("Matrice 2 :")
m3 = []
if len(m1)==len(m2):
    for i in range(0,len(m1)):
        m3.append(m1[i]*m2[i])
else:
    print("Incompatible sizes")
    
print(m3)
