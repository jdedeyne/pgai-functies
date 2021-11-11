# toegelaten
#   ord() en chr()
#   array.append()
#   len(array)
#   len(string)
#   string[index]
#   onderstaande functie isWhitespace(ch)



def isWhitespace(ch):
    return ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n'

def isAlpha(character):
    #ord('a') 97 ord('z') 122 ord('A') 65 ord('Z') 90 chr(91)
    return (65 <= ord(character) <= 90) or (97 <= ord(character) <= 122)

def isDigit(character):
    #ord 0 = 48, ord('9) == 57
    return 48 <= ord(character) <= 57

def isUpper(character):
    return (65 <= ord(character) <= 90)

def isLower(character):
    return (97 <= ord(character) <= 122)

def charToUpper(character):
    ret = character
    if isAlpha(character) and isLower(character):
        o = ord(character)
        ret = chr(o-32)
    return ret

def charToLower(character):
    ret = character
    if isAlpha(character) and isUpper(character):
        o = ord(character)
        ret = chr(o+32)
    return ret

def toLower(str):
    i=0
    ret = ''
    #overloop str, lower waar nodig.
    while i < len(str):
        ret += charToLower(str[i])
        i += 1
    return ret

def toUpper(str):
    i=0
    ret = ''
    #overloop str, upper waar nodig.
    while i < len(str):
        ret += charToUpper(str[i])
        i += 1
    return ret

def isGeheel(str):
    ret = True
    i=0
    while i < len(str) and ret == True:
        if isDigit(str[i]) or isWhitespace(str[i]) or str[i] == '-' or str[i] == '+':
            ret = True
        else:
            ret = False
        i+=1
    return ret

def trim(str):
    i=0
    skip = False
    ret1 = ''
    while i < len(str):
        if skip:
            ret1 += str[i]
        if not skip:
            if isWhitespace(str[i]):
                ret = ''
            else:
                ret1 += str[i]
                skip = True
        i+=1

    i=len(ret1)-1
    ret = ''
    skip = False
    while i >= 0:
        if skip:
            ret = ret1[i] + ret
        if not skip:
            if isWhitespace(ret1[i]):
                ret = ''
            else:
                ret = ret1[i] + ret
                skip = True
        i-=1

    return ret

def split(str, sep):
    woorden = []
    woord = ''
    i=0
    while i<len(str):
        if str[i] == sep:
            if len(woord) > 0 and woord != ' ':
                woorden.append(trim(woord))
                woord = ''
        else:
            woord += str[i]
        i+=1

    if len(woord) > 0 and woord != ' ':
        woorden.append(trim(woord))
        
    return woorden

def countDigit(str):
    ret = 0
    i=0
    while i<len(str):
        if isDigit(str[i]):
            ret += 1
        i+=1
    return ret

def countAlpha(str):
    ret = 0
    i=0
    while i<len(str):
        if isAlpha(str[i]):
            ret += 1
        i+=1
    return ret

def opgave1():
    str = input('Geef een zin in :')
    print('Aantal cijfers:', countDigit(str))
    print('Aantal letters:', countAlpha(str))
    
def getValidTransaction(str):
    transaction = 'D'
    amount = 0
    if charToUpper(str[0]) == 'D' or charToUpper(str[0]) == 'W':
        transaction = charToUpper(str[0])
        if str[1] == ' ':
            i=2
            getal = ''
            while i<len(str):
                if isDigit(str[i]):
                    getal += str[i]
                else:
                    #invalid char, break immediately
                    return 'D', 0
                i+=1
            amount = int(getal)

    return transaction, amount

def getNewTotal(total, str):
    t, a = getValidTransaction(str)
    if t == 'D':
        total = total + a
    else:
        if t=='W':
            if total -a >= 0:
                total = total - a
    return total

def opgave2():
    c = True
    total = 0
    while c:
        str = input()
        if str == '':
            c=False
        else:
            total = getNewTotal(total, str)
    print(total)

def special(d,n):
    spec = 0
    i = 0
    while i < n:
        spec = spec + d*10**i
        i += 1  
    return spec

def specialFaculteit(d,n):
    fac = 0
    i = 1
    while i <= n:
        fac = fac + special(d,i)
        i += 1  
    return fac

def opgave3():
    d = int(input('Cijfer:'))
    n = int(input('Aantal:'))
    print(specialFaculteit(d,n))

def move(x, y, direction, distance):
    
    if direction == 'U':
        y = y + distance
    if direction == 'D':
        y = y - distance
    if direction == 'L':
        x = x - distance
    if direction == 'R':
        x = x + distance
    return x,y

def parseMove(str):
    direction = 'U'
    distance = 0
    if charToUpper(str[0]) in ['U','D','L','R']:
        direction = charToUpper(str[0])
    if isDigit(str[2]):
        distance = int(str[2])
    return direction, distance

def doMove(x,y,str):
    direction, distance = parseMove(str)
    return move(x, y, direction, distance)

def opgave4():
    c = True
    x = 0
    y = 0
    while c:
        str = input()
        if str == '':
            c=False
        else:
            x,y = doMove(x,y, str)
    print('punt',x,y)
    print('afstand', int((x**2+y**2)**(1/2)))

def hasUpper(str):
    ret = False
    i=0
    while i<len(str):
        if isUpper(str[i]):
            return True
        i+=1
    return ret

def hasLower(str):
    ret = False
    i=0
    while i<len(str):
        if isLower(str[i]):
            return True
        i+=1
    return ret

def hasDigit(str):
    ret = False
    i=0
    while i<len(str):
        if isDigit(str[i]):
            return True
        i+=1
    return ret

def hasSpecialleke(str):
    ret = False
    i=0
    while i<len(str):
        if str[i] in ['$','#','@']:
            return True
        i+=1
    return ret

def hasSpatie(str):
    ret = False
    i=0
    while i<len(str):
        if str[i] in [' ']:
            return True
        i+=1
    return ret

def isValidPassword(str):
    
    if not hasUpper(str):
        return False
    if not hasLower(str):
        return False
    if not hasDigit(str):
        return False
    if not hasSpecialleke(str):
        return False
    if len(str) < 6:
        return False
    if len(str) >12:
        return False
    if hasSpatie(str):
        return False
    
    return True

def opgave5():
    print('begin opgave 5')
    if isValidPassword(input('test hier je paswoord:')):
        print('correct')
    else:
        print('niet correct')

#opgave1()
#opgave2()
#opgave3()
#opgave4()
#opgave5()