from random import *
for i in range(10):
    n=randint(1,10)
    m=randint(1,10)
    print("Question", i+1, ":", n,"x", m, "=")
    o=eval(input())
    if o == n * m :
          print("vrai")
    else :
        print("faux, la réponse est", n * m)


