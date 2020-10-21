n=int(input("Cb de nombre de Fibo tu veux ?? "))
p1=int(1)
p2=int(1)


if n > 2:
    print(p1)
    print(p2)
    for i in range(n-2):
        p3 = p1+p2
        print(p3)
        p1 = p2
        p2 = p3
elif n == 2:
    print(p1, p2)
elif n == 1:
    print(p1)
else:
    print("entre autre chose....")
    
