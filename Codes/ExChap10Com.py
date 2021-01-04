# Ex 3
'''
word = list(input("entrer un mot"))
word.sort()
print ("".join(word))
'''
# Ex 4
'''
liste = eval(input("Entrer une liste de produits et de prix. "))    #[p1, px1, p2, px2 ....]
                                                                    #[[p1, px1], 
                                                                    # [p2, px2] 
                                                                    #   ....
                                                                    # ]                                                                   
maxi = 0
for i in range(0,len(liste), 2):        
    if len(liste[i]) > maxi:
        maxi = len(liste[i])  

for i in range(0,len(liste), 2):        
    print(liste[i], (maxi - len(liste[i])) * " " + "$", '{:6.2f}'.format(liste[i+1] * 0.89))                                      

'''

# Ex 8
l = [i for i in range (1,1001) if i%7 == 0 and i%10 == 6]
print(l)
