# Schrijf een Python programma dat het spel ‘een 
# nummertje raden’ simuleert. Een door het spel 
# gegenereerd willekeurig getal tussen 0 en 100 moet 
# worden geraden. Het spel vraagt een getal en blijft 
# vervolgens hogere of lagere getallen vragen om de 
# speler te helpen. 
# De speler heeft 10 beurten. Als die op zijn is het spel 
# verloren. Als het getal wordt geraden is het spel 
# gewonnen en wordt ook aangegeven in hoeveel 
# beurten dat is gebeurd. Als de speler een negatief getal 
# ingeeft, wordt het spel afgebroken en wordt daarvan 
# melding gemaakt evenals in welke beurt dat gebeurde. 
# Hieronder zijn wij al aan het programma begonnen. Je 
# mag geen nieuwe variabelen meer introduceren. 
# Dit zijn de enige boodschappen die het programma op 
# het scherm mag zetten: 
# Geef een getal: 
# Geef een hoger getal: 
# Geef een lager getal: 
# Gewonnen in … beurten 
# Spel afgebroken in beurt … 
# Verloren

from random import * 
geheim = randint(0,100) #genereert een willekeurig getal tussen 0 en 100 
getal = int(input('Geef een getal [0-100]: ')) 
aantalIngelezenGetallen = 1 
while aantalIngelezenGetallen < 10:
    if getal < 0:
       print (f"Spel afgebroken in beurt {aantalIngelezenGetallen} ") 
    if getal == geheim:
        print(f"Gewonnen in {aantalIngelezenGetallen} beurten ")
        aantalIngelezenGetallen = 99
    else:
        if getal < geheim:
            getal = int(input('Geef een hoger getal: ')) 
        else:
            getal = int(input('Geef een lager getal: ')) 
    aantalIngelezenGetallen += 1
    
if aantalIngelezenGetallen == 10:
    print("Verloren")
