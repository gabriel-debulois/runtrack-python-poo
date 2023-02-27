class Personnage:
    def __init__(self, y=0, x=0):
        self.y = y
        self.x = x

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def position(self):
        return self.y, self.x


personnage = Personnage()

personnage.bas()
print(personnage.position())
personnage.droite()
print(personnage.position())
