def table(n):
    
    tab = []
    if n == 1:
        tab = [[0], [1]]
    else:
        L = table(n-1)
        for Li in L:
            tab.append(Li + [0])
            tab.append(Li + [1])
    return tab


n = int(input("n = "))
print(table(n))
