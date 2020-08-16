imiona = ["Bartek","Tomek","Andrzej",1,2,3,4,5]
print(imiona[1])
print(imiona[0:4])
print(imiona.index('Bartek'))
imiona.append('Wojtek')
imiona.insert(0,'Grzegorz')
print(len(imiona))

for czesc in imiona:
    print(czesc)

imiona.remove('Bartek')
del imiona[0]

print(imiona)

pierwszaLista = ['lampa','koc','mleko']
drugaLista = ['auto', 'dom', 'podroze']
print(pierwszaLista*8)
print(pierwszaLista + drugaLista)

pierwszaLista.sort()
print(pierwszaLista)
koc,lampa,mleko = drugaLista
print(koc)
print(lampa)
print(mleko)

