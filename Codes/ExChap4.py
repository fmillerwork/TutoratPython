from random import randint
#Ex6
'''
nbItems = int(input("Items to buy ? "))
itemCost = 0
if nbItems < 10 and nbItems > 0:
    itemCost = 12
elif nbItems >= 10 and nbItems <= 99:
    itemCost = 10
elif nbItems > 99:
    itemCost = 7
else :
    print("not valid number...")

if itemCost != 0:
    print(nbItems * itemCost)
'''

#Ex8
#Année bisextile => divisible par 400
#                => divisible par 4 et non par 100
'''
year = int(input("Enter a year : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year !")
else : 
    print(year, "is NOT a leap year !")
'''

#Ex10
'''
for i in range(10):
    nb1 = randint(1,9)
    nb2 = randint(1,9)
    print("Question 1:", nb1, "x",nb2 , "=", end=" ")
    if int(input("")) == nb1 * nb2:
        print("Rigth !")
    else : 
        print("Wrong. The answer is ", nb1 * nb2)
'''
