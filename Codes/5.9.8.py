x = eval(input("x = "))
y = eval(input("y = "))
z = eval(input("z = "))

tempX = x #variable temporaire pour stocker la valeur de x

x = y
y = z
z = tempX

print("x =" ,x ,"y =" ,y ,"z =", z)