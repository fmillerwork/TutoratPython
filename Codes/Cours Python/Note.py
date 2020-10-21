'''
COMMENTAIRE

'''

n = int(input("Entre une note : "))
if n > 0:
    if n<10:
        print("repasse le bac")
    elif n<12:
        print("ok")
    elif n<14:
        print("AB")
    elif n<16:
        print("B")
    else:
        print("TB")
else :
    print("Entre autre chose")
