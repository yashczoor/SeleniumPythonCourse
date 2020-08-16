class Pies:
    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek):
        print('wewnatrz metody init')
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print("woof woof")
    #     return "Hau! Hau!"

    def zaprezentujSie(self):
        print('rasa to ' + self.rasa)
        print('wiek psa to ' + str(self.wiek))
        print('Ma na imie ' + self.imie)


reksio = Pies('kundel','Reksio',8)
# print(reksio.wiek)
# reksio.wiek = 9
# print(reksio.wiek)
# reksio.gatunek = 'ptak'
# print(reksio.gatunek)
reksio.szczekaj()
print(reksio.szczekaj()) #bo nic nie zwraca tylko robi
reksio.zaprezentujSie()
