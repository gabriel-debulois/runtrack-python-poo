class Cercle:
    def __init__(self, r):
        self.r = r

    def circonference(self):
        circonference = self.r * self.r * 3.14
        return circonference

    def air(self):
        air = (2 * 3.14) * self.r
        return air

    def diametre(self):
        diametre = self.r * self.r
        return diametre

    def changerRayon(self, r):
        self.r = r

    def afficherInfos(self):
        print("diametre =", self.diametre())
        print("air=", self.air())
        print("circonference =", self.circonference())


cercle = Cercle(4)
cercle.afficherInfos()
cercle.changerRayon(7)
cercle.afficherInfos()

