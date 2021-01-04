#Ex 2
'''
def add_excitement(liste):
    for i in range(len(liste)):
        liste[i] = liste[i] + "!"
    
l = ["abc", "def", "ghi"]
add_excitement(l)   
print(l)    


def add_excitement1(liste):
    l = []
    for i in range(len(liste)):
        l.append(liste[i] + "!")
    return l
    
liste = ["abc", "def", "ghi"]
print(add_excitement(liste))   
print(liste) 
'''
#Ex 6
'''
def binom(n,k):
    nFact = 1
    kFact = 1
    nkFact = 1
    for i in range(1,n+1):
        nFact *= i
    for i in range(1,k+1):
        kFact *= i
    for i in range(1,(n-k)+1):
        nkFact *= i
    return nFact / (kFact * nkFact) 

print(binom(3,1))
'''

#Ex 8
'''
def numbers_of_factor(n) :
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return(count)

print(numbers_of_factor(10))
'''

#Ex 9
'''
def factors (n) :
    list = []
    for i in range(1,n+1):
        if n % i == 0:
            list.append(i)
    return(list)
print(factors(50))
'''

#Ex 10
"""
from random import randint
def closest(L,n):
    L2 = L
    L2.sort()
    for i in range(len(L2)):
        if L[i] > n:
            return L[i-1]

print(closest([1,2,8,5,47,9,521],15))
"""

#Ex 13
#string.isupper()
def change_case(s):
    newString = ""
    for carac in s:
        if str(carac).isupper():
            newString += str(carac).lower()
        elif str(carac).islower():
            newString += str(carac).upper()
        else :
            newString += str(carac)
    return newString

print(change_case("BonjOUur AbCE"))