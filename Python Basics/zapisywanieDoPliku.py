# file = open('nowy.txt', 'w') #nadpisze zmiany
file = open('nowy.txt', 'a') #dopisze kolejne
file.write('Tekst testowy \n')
file.close()