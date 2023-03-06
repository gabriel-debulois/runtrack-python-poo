class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

# Recupères les valeurs

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def __verifier_plein(self):
        return self.__reservoir

# Modifies les valeurs

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def demarrer(self):
        if not self.get_en_marche() and self.__verifier_plein() > 5:
            self.set_en_marche(True)
            print("Voiture démarrer")
        else:
            if self.__verifier_plein() <= 5:
                print("impossible de démarrer car le resevoir est vide")
            else:
                print("Déjà en marche")

    def arreter(self):
        if self.get_en_marche():
            self.set_en_marche(False)
            print("Voiture arrêter")
        else:
            print("Déjà à l'arrêt")




voiture = Voiture("twingo", "pouet", 2016, 50)
voiture.demarrer()
voiture.arreter()
voiture.set_reservoir(1)
voiture.demarrer()




