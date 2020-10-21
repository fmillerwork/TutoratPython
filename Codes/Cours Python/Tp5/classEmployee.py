class Employee:
     numberEmpls = 0
     
    #constructeur
    def __init__(self, first, name, salary):#seld est un objet de type Employee
        self.first=first
        self.name=name
        self.salary=salary
        Employee.numberEmpls += 1 #variable static
        
    def fullName(self):
        return self.first + " " + self.name
    
    def __repr__(self): #toString
        return self.fullname()
    
class Developer(Employee): #héritage
    
    def __init__(self, first, name, salary, pro_lang):
        Employee.__init__(self, first, name, salary)
        self.pro_lang = prp_lang

    

emp1 = Employee("Marc", "Marlot", 2500)
print(emp1.salary)
print(emp1.fullName())

dev1=Developer("Sam", "Marcle", 3000, "Java")

#true ou false selon la class d'origine de l'instance
print(isinstance(emp1, Employee))



#None = null en python

#if x in tab
#if y not in tab
