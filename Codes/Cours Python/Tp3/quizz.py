from random import*

Countries=['Afghanistan','Albania', 'Argentina','Austria','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Bermuda','Bhutan','Bolivia']
Capital=["Kabul",'Tirana','Buenos Aires','Vienna','Nassau','Manama','Dhaka','Bridgetown','Minsk','Brussels','Hamilton','Thimphu','Sucre']
Currency=["Afghani","Lek", "Peso","Euro","Bahamian Dollar","Bahraini dinar","Taka","Barbadian Dollar","Belarusian ruble","Euro","Bermudian Dollar","Bhutanese ngultrum","Boliviano"]
Continent=["Asia","Europe",'South America',"Europe","North America","Asia","Asia","North America","Europe","Europe","North America","Asia","South America"]


for quest in range(1,10):
    countryNb = randint(1,13)
    country = Countries[countryNb]
    parameter = randint(1,3)
    if parameter == 1:
        paramStr = "capital"
    if parameter == 2:
        paramStr = "currency"
    if parameter == 3:
        paramStr = "continent"
    print("What is the ", paramStr, "of", country, "?")
    answer = input("Réponse :")
    
    if parameter == 1 and Capital[countryNb] == answer:
        print("True answer!")
    elif parameter == 2 and Currency[countryNb] == answer:
        print("True answer!")
    elif parameter == 3 and Continent[countryNb] == answer:
        print("True answer!")
    else:
        print("Wrong answer!")

print("End of quizz ;)")
