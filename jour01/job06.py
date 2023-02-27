class Animal:
    def __init__(self, age=0, nom=""):
        self.age = age
        self.nom = nom

    def age(self):
        return self.age

    def viellir(self):
        self.age +=1

    def nommer(self, nom):
        self.nom = nom
        return nom


animal = Animal()
print("l'age de l'animal", animal.age, "age")
animal.age = 10
print("l'age de l'animal", animal.age, "age")
animal.viellir()
print("l'age de l'animal", animal.age, "age")

print("l'animal se nomme", animal.nommer("Robert"))
