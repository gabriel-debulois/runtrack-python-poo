class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def get_livre(self):
        print("titre:", self.__titre,
              "\nauteur:", self.__auteur,
              "\nnombre de page:", self.__pages)

    def set_livre(self, titre, auteur, pages):
        if self.__pages <= 0 or self.__pages != int:
            print("Page est inferieur ou égal à 0")
        else:
            self.__titre = titre
            self.__auteur = auteur
            self.__pages = pages

    def verification(self):
        return print(self.__disponible)

    def emprunt(self):
        if self.__disponible:
            self.__disponible = False
            print("Livre emprunter")
        else:
            print("Livre indisponible")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Livre rendu")




livre1 = Livre("Un livre", "Richard", 50)
livre1.verification()
livre1.emprunt()
livre1.emprunt()
livre1.rendre()
livre1.verification()