class Ville:
    def __init__(self, nomville, nHabitant):
        self.__nomville = nomville
        self.__nHabitant = nHabitant

    def get_nombre(self):
        return self.__nHabitant

   # def add_nombre(self, nHabitant):
    #    self.__nHabitant += nHabitant

    def villeInfos(self):
        print("La ville est", self.__nomville, "avec", self.__nHabitant, "habitant")


class Personne(Ville):
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    #def ajouterPopulation(self):
     #   Ville.add_nombre(1)



marseille = Ville("Marseille", 861635)
paris = Ville("paris", 1000000)
marseille.villeInfos()
paris.villeInfos()

