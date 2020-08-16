imie = "Piotr"
nazwisko = "'Jaroszuk'"
adres = '''Kwiatowa 28c/1 Warszawa 00-000'''

print(nazwisko)
print(adres)

print("\\Czytam \t ksiazke \n\"Wladca P\"")

print('male litery'.upper())
print("WIELKIE".lower())

print(imie.islower())
print(nazwisko.isupper())
print(imie[0])
print(imie[0:4])
print(imie.index('r'))
print("Ala" in "Ala ma kota")
print("Kasia" not in "Ala ma kota")

print(" ".join(['kisiel','ciastka','Alicja']))
print("ale, jaja, były, nie".split(", "))
print(imie.startswith('Pi'))
print(nazwisko.endswith('okokok'))
