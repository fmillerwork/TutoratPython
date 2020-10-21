def digitalRoot(n):
    sum = 0
    if(len(str(n))==1):
        return n
    else:
        for i in range(len(str(n))):
            sum = sum + int(str(n)[i])
        return digitalRoot(sum)
    


print(digitalRoot(int(input("Entre en nb "))))
