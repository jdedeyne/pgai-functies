from random import *

geheim = randint(0,100) #genereert een willekeurig getal tussen 0 en 100
getal = int(input('Geef een getal [0-100]: '))
aantalIngelezenGetallen = 1

while getal != geheim and aantalIngelezenGetallen < 10 and getal > 0:
    if getal < geheim:
        print('Geef hoger een getal [0-100]: ', end = '')
    else:
        print('Geef lager een getal [0-100]: ', end='')
    getal = int(input())
    aantalIngelezenGetallen += 1

if getal == geheim:
    print('Gewonnen in', aantalIngelezenGetallen, 'beurten')
elif getal < 0:
    print('Spel afgebroken in beurt', aantalIngelezenGetallen)
else:
    print('Verloren')