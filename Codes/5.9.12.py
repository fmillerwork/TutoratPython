from random import randint
score = 0

for i in range(5):
    reponse = randint(1,10)
    
    n = int(input("essai : "))
    while n != reponse:
        score += 1
        n = int(input("essai : "))
    score += 10
    print("Gagné !\n")
print(score)
