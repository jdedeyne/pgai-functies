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

def keerOm(getal):
    ret=nan
    if getal<0:
        ret='-'
    rev=''
    for let in str(abs(getal)):
        rev = let + rev
    ret = int(ret + str(int(rev)))
    return ret

def faculteit(getal):
    ret = ''
    if getal<=0:
        ret = 1
    else:
        sub = 1
        for x in range(0,getal):
            sub = sub * (getal-x)
        ret = sub
    return ret

def gemiddelde(getallen):
    ret = nan
    if len(getallen) > 0:
        sum = 0
        for g in getallen:
            sum += g
        ret = sum/len(getallen)        

    return ret

def grootstePriemKleinerDanOfGelijkAan(bovengrens):
    ret = nan
    zeef=[0]*(bovengrens+1)
    priem=[0]*(bovengrens+1)
    #1 toch opnemen
    #priem[1] = 1
    #beginnen bij 2
    i=2
    while i<=bovengrens:
        #print('check',i)
        if zeef[i] == 0:
            #print('priem',i)
            priem[i]=1
            zeef[i]=1
            j=1
            while j*i<=bovengrens:
                #print('check zeef',j*i)
                if zeef[j*i]==0:
                    zeef[j*i]=1
                j+=1
        i+=1
    i=1
    while i<=bovengrens:
        if priem[i]==1:
            ret = i
        i+=1

    return ret

def variatie(n, k):
    ret = nan
    if k>n or n<0 or k<0:
        ret = 0
    else:
        if n==0 and k==0:
            ret = 1
        else:
            if k == 1:
                ret = n
            else:
                teller=n
                i=teller-1
                if n!=k:
                    noemer=(n-k)
                else:
                    noemer=1
                while i>0:
                    teller *= i
                    if i<(n-k):
                        noemer *=i
                    i-=1
                ret = int(teller/noemer)
    return ret