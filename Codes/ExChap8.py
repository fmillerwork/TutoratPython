#Ex1 

#6 lignes
articles = ["a", "an", "the"]
text = input("Enter some text : ")
count = 0
for article in articles:
    count += text.count(" " + article + " ")
print(count)


'''
#4 lignes
articles = ["a", "an", "the", "A", "An", "The"]
text = input("Enter some text : ")
textArticles = [mot for mot in text.split() if articles.count(mot) != 0]
print(len(textArticles))


'''














#Ex4
'''
from random import shuffle

sentence = input("Enter a sentence : ")
sentenceList = sentence.split()
shuffle(sentenceList)
print(" ".join(sentenceList))

sentence = sentence.lower()
sentenceList = sentence.split()
shuffle(sentenceList)
sentence = " ".join(sentenceList)
sentence = sentence.replace(".", "")
sentence = sentence[0].upper() + sentence[1:] + "."
print(sentence)
'''

#Ex10
#text = input("Entrer un texte :")
'''
text = """Oh shoot, I thought I had the dang problem
figured out. Darn it. Oh well, it was a heck of a freakin try."""

cursedWords = ["shoot", "darn", "dang", "freakin", "heck", "shoot"]
for i in range(len(cursedWords)): #bonne pratique de mettre len(cursedWords) au lieu de la longueur en brute (car fonctionne toujours si on souhaite ajouter d'autres mots)
    text = text.replace(cursedWords[i],len(cursedWords[i]) * "*")
print(text)
'''

