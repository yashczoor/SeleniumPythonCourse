import random

def generujLiczbe(max):
    return random.randint(0,max)

i = 0
max = 7

while not i == max:
    i = generujLiczbe(max)
    print(i)