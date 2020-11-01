print('Ex 2.9')
n = eval(input('Enter how many Fibonacci number to print: '))
f1 = 1
f2 = 1
print(f1 ,f2 , sep=", ",end = ', ')
for i in range(n):
    f3 = f1 + f2
    print(f3, end = ', ')
    f1 = f2
    f2 = f3
print()