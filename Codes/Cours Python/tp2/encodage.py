cav="abcdefghijklmnopqrstuvwxyz"
enc="azertyuiopqsdfghjklmwxcvbn"

"""print(cav.index("g")) #première indice où "g" est présent"""
n=input("texte :")

text=""
for a in n:
    for b in cav:
        if a == b:
           text += enc[cav.index(b)]
print(text)
                       

