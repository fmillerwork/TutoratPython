#exercice 1
dividende=int(input("Quel est le dividende ?"))
diviseur=int(input("Quel est le diviseur ?"))
precision=int(input("Quelle est la précision voulue ?"))
print dividende,(precision-1)*" " ,"|" ,diviseur
print 2*precision*"-"# les espaces sont proportionels avec la precision
for i in range (0,precision):
    reste=dividende-(dividende//diviseur)*diviseur #formule de maths pour trouver le reste
    print (i+1-(len(str(reste))))*" ",reste,(precision-i)*" ","|", (i+(2-(len(str(dividende//diviseur)))))*" ",dividende//diviseur
    dividende=reste*10



    # exercice 2
from random import randint
scoreOrdi=0
scoreU=0
pierre=1
feuille=2
ciseau=3
for i in range (1,6):#nous voulons seulement 5 parties
  ChoixU=int(input("Choisissez entre pierre, feuille ou ciseaux"))
  ChoixOrdi=randint(1,3)
  print("Pour la partie numero", i,"le choix de l'utilisateur est",ChoixU,"et le choix de l'ordinateur est", ChoixOrdi)
  if ChoixU== 1 and ChoixOrdi==2:# la feuille est plus forte que la pierre
      print "l'ordinateur gagne"
      scoreOrdi=scoreOrdi+1
  if ChoixU== 2 and ChoixOrdi== 3: #ciseau est plus fort que la feuille
      print "l'ordinateur gagne"
      scoreOrdi=scoreOrdi+1
  if ChoixU== 3 and ChoixOrdi== 1: #pierre est plus fort que ciseau
      print "L'ordinateur gagne"
      scoreOrdi=scoreOrdi+1
  if  ChoixU==1 and ChoixOrdi==3:
      print "L'utilisateur gagne"
      scoreU=scoreU+1
  if ChoixU==2 and ChoixOrdi==1:
      print "L'utilisateur gagne"
      scoreU=scoreU+1
  if ChoixU==3 and ChoixOrdi==2:
      print "l'utilisateur gagne"
      scoreU=scoreU+1
  if ChoixU==ChoixOrdi:
      print "egalite"
  if scoreOrdi>scoreU and i==5:
      print "L'ordinateur gagne la partie", scoreOrdi, "a", scoreU
  if scoreOrdi<scoreU and i==5:
      print "Vous gagnez la partie",scoreU, "a", scoreOrdi
  if scoreOrdi==scoreU and i==5:
      print "Pas de vainqueur", scoreU, "partout"