class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

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


livre1 = Livre("Un livre", "Richard", 50)
livre1.get_livre()
livre1.set_livre("Un livre", "Chat", 1.2)
livre1.set_livre("Un livre", "Chat", -10)
livre1.get_livre()
