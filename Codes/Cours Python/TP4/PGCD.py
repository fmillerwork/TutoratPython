a=int(input("a = "))
b=int(input("b = "))
if a >=b:
    max = a
    min = b
else:
    max = b
    min = a


while min != 0:
    remainder = max%min
    max = min
    min = remainder

print(max)
