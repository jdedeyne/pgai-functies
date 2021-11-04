from math import *

# toegelaten
#   len(array)
#   nan (vanaf Python 3.5)

def ggd(getal1, getal2):
    rest = 1
    grootste = 0
    kleinste = 0

    if getal1 > getal2:
        grootste=getal1
        kleinste=getal2
    else:
        grootste=getal2
        kleinste=getal1

    while rest != 0:    
        rest = grootste%kleinste
    if rest != 0:
        grootste=kleinste
        kleinste=rest
    
    return kleinste

def keerOm(x):
    return x

def faculteit(x):
    return x

def gemiddelde(x):
    return None

def grootstePriemKleinerDanOfGelijkAan(x):
    return None

def variatie(x):
    return None