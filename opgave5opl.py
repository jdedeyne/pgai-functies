
def extreme(array, min=True):
    i = 0
    extreme = None
    while i < len(array):
        if extreme == None:
            extreme = array[i]
        if min:
            if array[i] < extreme:
                extreme = array[i]
        else:
            if array[i] > extreme:
                extreme = array[i]
        i+=1
    return extreme

def shiftToPositive(array):
    arrExtreme = extreme(array)    
    ret = []
    if arrExtreme < 0:
        i=0
        while i<len(array):
            ret.append(array[i]-arrExtreme)
            i+=1
    else:
        ret = array
    return ret

def sumOf(array):
    i=0
    ret=0
    while i<len(array):
        ret += array[i]
        i+=1
    return ret

def distribution(array):
    ret = copyOf(array)
    ret = shiftToPositive(ret)
    tot = sumOf(ret)
    i=0
    while i<len(ret):
        ret[i]=ret[i]/tot
        i+=1
    return ret

def histogram(array, precision=0):
    low = int(extreme(array)*10**precision)
    high = int(extreme(array, min=False)*10**precision)
    temp = [0]*(high-low+1)
    i=0
    while i<len(array):
        index = int(array[i]*10**precision-low)
        temp[index] += 1
        i+=1
    
    return temp
    

def copyOf(array):
    ret = []
    i=0
    while i<len(array):
        ret.append(array[i])
        i+=1
    return ret

def sort(array):
    low = extreme(array)
    high = extreme(array, min=False)
    temp = [0]*(high-low+1)
    i=0
    while i<len(array):
        temp[array[i]-low] += 1
        i+=1
    i=0
    j=0
    while i<len(temp):
        if temp[i]>0:
            array[j] = (i+low)
            j+=1
        i+=1
    return array

def sortedCopyOf(array):
    ret = copyOf(array)
    ret = sort(ret)
    return ret