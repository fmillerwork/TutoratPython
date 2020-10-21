nb = int(input("number to convert "))
binar=[]

while nb != 0:
    binar.append(nb%2)
    nb=nb//2
    if nb//2 == 0:
        binar.append(nb%2)
        break
    
print (binar[::-1])
