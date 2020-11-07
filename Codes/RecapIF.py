print("\n-----------if-----------")

print("introduction :")
a = eval(input("a = "))
b = eval(input("b = "))
if a < b :
    print("a < b")
elif a == b: #Python ne regarde la condition d'un elif que si aucune condition d'un if ou elif situé au dessus n'a été Vraie.
    print("a = b")
else : # => elif a > b
    print("a > b")

print("\nelif VS if :")
a = 2
b = 6
if a != b :
    print("a != b")
elif a < b : #on n'entre pas dans ce elif car la condition du if au dessus est vraie (True)
    print("elif")
if a < b : 
    print("if")


print("\nOpérateurs :")
print("Opérateurs de comparaison possibles :", "<", ">", "<=", ">=", "== (égal à ...) | attention à la confusion avec =", "!= (différent de ...)", sep="\n\t")
print("Opérateurs supplémentaires :", "and (ET logique : toutes les conditions doivent être vraies)", "or (OU logique => 'et/ou' : au moins 1 condition doit être vraie)", "not (négation de la condition)", sep="\n\t")
a = 5
b = 8
nb = eval(input("nb = "))
if nb < b and nb > a:
    print("a < nb < b (and)")
if nb < b or nb > a:
    print("nb < b OU nb > a OU a < nb < b (or)")
if nb < b and nb > a or nb == 10: # => if (nb < b and nb > a) or nb == 10   Les and sont traités avant les or. Donc si besoin de traiter les or en premier, il faut mettre des parenthèses (comme pour les calculs). Dans le doute, toujours parenthèser, c'est plus clair.
    print("a < nb < b OU nb = 10")

print("\nType booléen (boolean en anglais) :")
a = True #ON, 1, vrai, ...
b = False #OFF, 0, faux, ...

if a: # if a == True
    print("a est Vrai")
else:
    print("a est Faux")
if b: # if b == True
    print("b est Vrai")
else:
    print("b est Faux")