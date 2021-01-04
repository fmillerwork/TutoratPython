#Ex 1
'''
articles = ["a", "an", "the", "A", "An", "The"]
text = input("Enter some text : ")
textArticles = [mot for mot in text.split() if articles.count(mot) != 0]
print(len(textArticles))
'''

#Ex4
'''
from random import shuffle
tense = input('Entrez une phrase')
tenseList = tense.split()
shuffle(tenseList)
print(" ".join(tenseList))



from random import shuffle
tense = input('Entrez une phrase:')
tense = tense.lower()
tenseList = tense.split()
shuffle(tenseList)
newTense = " ".join(tenseList)
newTense = newTense.replace(".","")
print(newTense[0].upper() + newTense[1:] + ".")
'''

#Ex 10
text = """Oh shoot, I thought I had the dang problem
figured out. Darn it. Oh well, it was a heck of a freakin try."""

cursedWords = ["shoot", "darn", "dang", "freakin", "heck"]
for word in cursedWords:
    text = text.replace(word, "*" * len(word))
print(text)


