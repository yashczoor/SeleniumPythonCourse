dziennik = {1:"kowalski",2:"nowak",3:"lewandowski"}

print(dziennik.get(1))
print(dziennik[1])
dziennik[4]='Mucha'
print(dziennik[4])

for key in dziennik.keys():
    print(key)

for val in dziennik.values():
    print(val)

del dziennik[1]
print(dziennik.keys())