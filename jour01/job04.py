class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)


Personne("Gabriel", "Debulois").SePresenter()
Personne("Raphael", "Rossignol").SePresenter()
