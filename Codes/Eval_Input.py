a = eval(input("\nEntre un int :\n"))
print("Type :", type(a)) #<class 'int'> car eval() converti le string donné par input() en int

a = eval(input("\nEntre un float :\n"))
print("Type :", type(a)) #<class 'float'> car eval() converti le string donné par input() en float

a = eval(input("\nEntre quelque chose (lettres et/ou nombre) avec \"\":\n"))
print("Type :", type(a)) #<class 'str'> car on a explicitement dit que c'est un string avec les ""

a = input("\nEntre quelque chose (lettres et/ou nombre) sans \"\":\n")
print("Type :", type(a)) #<class 'str'> car input() seul donne toujours un string

a = input("\nEntre quelque chose (lettres et/ou nombre) avec \"\":\n")
print("Type :", type(a)) #<class 'str'> car input() seul donne toujours un string


