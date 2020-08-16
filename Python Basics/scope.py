imie = "Bartek"
nazwisko = "Nowak"

def przedstawSie():
    global nazwisko #nadpisuje zmienna globalna z poziomu metody
    nazwisko = 'Kowalski' #ta lokalna zmienna jest wazniejsza
    print(nazwisko)
    print(imie)

print(imie)
print(nazwisko)
przedstawSie()
print(nazwisko)
