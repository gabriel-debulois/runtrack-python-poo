class Student:
    def __init__(self, prenom, nom, nEtudiant, credit=0):
        self.__prenom = prenom
        self.__nom = nom
        self.__nEtudiat = nEtudiant
        self.__credit = credit

    def add_credit(self, credit):
        if credit <= 0:
            print("Valeur inferieur ou égal à 0")
        else:
            self.__credit += credit

    def studenInfo(self):
        print("Prenom:",self.__prenom,
        "\nNom:",self.__nom,
        "\nNuméro étudiant:",self.__nEtudiat,
        "\nNiveau:", self.eval())

    def get_credit(self):
        print("Le nombre de credits de", self.__prenom, self.__nom, "est de", self.__credit)

    def eval(self):
        return self.__studentEval()

    def __studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        if self.__credit >= 80:
            return "Très bien"
        if self.__credit >= 70:
            return "Bien"
        if self.__credit >= 60:
            return "Passable"
        if self.__credit < 60:
            return "Insuffisant"


student = Student("John", "Doe", 145)
student.add_credit(10)
student.add_credit(20)
student.add_credit(40)
student.get_credit()
student.studenInfo()
