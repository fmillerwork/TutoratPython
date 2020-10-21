i = 1
def f(n):
    global i  #pour pouvoir utiliser une variable globale
    n = n +1
    return n

def f1(n):
    n = n + 1
def f2(l):
    l.append(100)
    
a = 1
m = [1,2,3]
a=f1(a)
f2(m)
print(a,m)




