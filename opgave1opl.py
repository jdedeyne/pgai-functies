from math import *

# toegelaten
#   len(array)
#   nan (vanaf Python 3.5)

def ggd(getal1, getal2):
    rest = 1
    grootste = getal1
    kleinste = getal2

    while rest != 0:    
        rest = grootste % kleinste
        if rest != 0:
            grootste = kleinste
            kleinste = rest
    
    return kleinste

def keerOm(getal):
    sign = 1
    res = 0
    if getal < 0:
        sign = -1
        getal = -getal

    while getal > 0:
        res = res * 10 + (getal % 10)
        getal = getal // 10

    return res*sign

def faculteit(getal):
    ret = 1
    for i in range(2, getal + 1):
        ret *= i
    return ret

def gemiddelde(getallen):
    ret = nan
    if len(getallen) > 0:
        sum = 0
        for i in range(0, len(getallen)):
            sum += getallen[i]
        ret = sum/len(getallen)        

    return ret

def grootstePriemKleinerDanOfGelijkAan(bovengrens):
    ret = nan
    zeef = [0]*(bovengrens+1)
    i = 2
    laatstgevondenpriem = nan
    while i <= bovengrens:
        if zeef[i] == 0:
            zeef[i] = 1
            laatstgevondenpriem = i

            for j in range(1, (bovengrens//i)+1):
                zeef[j*i] = 1
        i += 1

    return laatstgevondenpriem

def variatie(n, k):
    if (n >= k) and (k >= 0):
        res = 1
        i = n
        while i > n-k:
            res *= i
            i -= 1
    else:
        res = 0
    return res