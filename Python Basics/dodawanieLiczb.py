while True:
    try:
        print("Podaj pierwsza liczbe:")
        pierwszaLiczba = int(input())
        print('Podaj druga')
        drugaLiczba = int(input())
        print(pierwszaLiczba + drugaLiczba)
        break
    except ValueError:
        print("podałeś błędną wartość")
        print('sproboj ponownie')
        # continue
