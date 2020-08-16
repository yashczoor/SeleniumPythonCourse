class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstawSie(self):
        return "Nazywam sie " + self.imie + ' ' + self.nazwisko

class Student(Osoba):
    def __init__(self,imie,nazwisko,numerIndeksu):
        Osoba.__init__(self,imie,nazwisko)
        self.indeks = numerIndeksu

    def podajNumerIndeksu(self):
        return self.indeks

    # def przedstawSie(self):
    #     return "Jestem studentem " + self.imie + ' ' + self.nazwisko
    # ta metoda nadpisze metodę z klasy rodzica
student = Student('Tomasz',"Kot",123456)
print(student.przedstawSie())
print(student.podajNumerIndeksu())


