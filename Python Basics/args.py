def rzeczy(pierwszaRzecz, *args):
    print(pierwszaRzecz)
    # print(args[0])
    for arg in args:
        print(arg)

def dziennik(klasa='1c',**kwargs): #parametr domyslny
    print('Klasa ' + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
        print(kwargs.get(nazwisko))

dziennik(Kowalski=1,Nowak=2,Wisniewski=3)
# dziennik('3c', Kowalski=1,Nowak=2,Wisniewski=3)
rzeczy('lampa','a','b','c','kotek')


