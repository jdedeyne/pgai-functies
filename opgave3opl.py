# toegelaten
#   array.append()
#   len(array)
#   len(string)
#   string[index]

def substr(checkstr, start, length):    
    actstart = start    
    if start < 0:
        actstart = len(checkstr) + start        
    actend = actstart + length
    if actend < actstart:
        temp = actstart
        actstart = actend
        actend = temp

    i=actstart
    ret = ''
    while i>=0 and i<actend and i<len(checkstr):
        ret += checkstr[i]
        i+=1
        
    return ret

def reverse(checkstr):
    i=0
    lengte = len(checkstr)
    ret = ''
    if lengte == 0:
        return ''
    while i< lengte:
        ret += checkstr[lengte-1-i]
        ## increase counter
        i+=1
    return ret

def isPalindrome(checkstr):
    i=0
    lengte = len(checkstr)
    if lengte == 0:
        return False
    while i< lengte/2:
        if checkstr[i] != checkstr[lengte-1-i]:
            return False
        ## increase counter
        i+=1
    return True

def find(zoekstr, instr, index = 0):
    #profile str
    zoeklen = len(zoekstr)
    #start vanaf index
    i = index
    #vergelijk window met str
    windowstr = ''
    while i < len(instr):
        #create window
        windowstr += instr[i]
        #slide the window if necessary
        if len(windowstr) > len(zoekstr):
            j = 1
            tempstr = ''
            while j<len(windowstr):
                tempstr += windowstr[j]
                j+=1
            windowstr = tempstr
        #compare window with searchstr
        if windowstr == zoekstr:
            return i-len(zoekstr)+1                    
        i+=1
    #nothing found -> return -1
    return -1

def findAll(zoekstr, instr, index=0):
    #start from requested index
    i = index
    #store results in array
    ret = []
    #loop untill we find nothing -> i == -1
    while i != -1:
        #find first occurence
        i = find(zoekstr, instr, i)
        #if not -1, add to results, increase position
        if i != -1:
            ret.append(i)
            i+=1
    return ret

def replace(zoekstr, tostr, instr):
    #zoek alle instances
    inst = findAll(zoekstr, instr, index=0)
    if len(inst) > 0:
        i = 0
        ret=''
        while i<len(instr):
            if i in inst:
                ret += tostr
                if len(tostr) > 0:
                    j=i+1
                    while j<i + len(zoekstr)-1:
                        if j in inst:
                            ret += tostr
                        j+=1
                    i = len(ret)-1
                else:
                    i = i + len(zoekstr) -1
            else:
                ret += instr[i]
            i+=1
    else:
        ret = instr
    return ret

def decompose(digit):
    ret = []
    strDigit = str(digit)
    i = len(strDigit)-1
    while i >= 0:
        ret.append(int(strDigit[i]))
        i-=1

    return ret

def singleDigitInDutch(digit):
    dutch = ['nul','een','twee','drie','vier','vijf','zes','zeven','acht','negen']
    return dutch[digit]

def doubleDigitInDutch(digit, hashundred=False, hasthousand=False):
    tientjes = ['nul','een','twee','drie','vier','vijf','zes','zeven','acht','negen','tien','elf','twaalf','dertien','veertien','vijftien','zestien','zeventien','achttien','negentien']
    tientallen=['nultig', 'tientig', 'twintig','dertig','veertig','vijftig','zestig','zeventig','tachtig','negentig']
    ret = ''
    if digit < 20:
        ret =  tientjes[digit]
        if digit < 10 and hashundred:
            ret = 'en' + ret
        if digit == 0 and hashundred:
            ret = ''
        if digit == 1 and hasthousand:
            ret = ''
    else:
        tiental = digit//10
        eental = digit%10
        join = 'en'
        if substr(tientjes[eental],-1,1) == 'e':
            join='ën'
        ret =  tientjes[eental] + join + tientallen[tiental]
        
    return ret


def inDutchThreeDigit(digit, hasthousand=False):
    dig = decompose(digit)
    ret = NotImplemented
    if digit < 100:
        ret = doubleDigitInDutch(digit, False, hasthousand)     
    else:
        honderdtal = digit//100
        rest = digit%100
        if honderdtal == 1:
            ret = 'honderd'        
        if honderdtal > 1:
            ret = doubleDigitInDutch(honderdtal) + 'honderd'
        ret = ret + doubleDigitInDutch(rest, True, hasthousand)
    return ret

def inDutch(digit):
    ret = ''
    rest = digit
    if rest > 1000000:
        miljoenen = digit//1000000
        rest = digit%1000000
        ret = inDutchThreeDigit(miljoenen) + ' miljoen'
    if rest > 1000:
        duizenden = rest//1000
        rest = rest%1000
        ret = ret + ' ' + inDutchThreeDigit(duizenden, True) + 'duizend'
    ret = ret + ' ' + inDutchThreeDigit(rest, False)
    return ret