from datetime import *

# toegelaten
#   functie today

def today():
    now = datetime.today()
    return now.year, now.month, now.day

def isLeapYear(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return True
    return False

def numberOfDaysIn(year, month=0):
    if month==0:
        if isLeapYear(year):
            return 366
        else:
            return 365
    else:
        months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if isLeapYear(year) and month == 2:
            return 29
        else:
            return months[month]
    return NotImplemented

def numberOfDay(year, month, day, sinceYear=-1):
    i=1
    ret = 0
    if sinceYear != -1:
        j=sinceYear
        while j < year:
            ret += numberOfDaysIn(j)
            j+=1
    while i<month:
        ret +=numberOfDaysIn(year, i)
        i+=1
    ret += day
    return ret

def remainingNumberOfDayInYear(year, month, day):
    jaardag = numberOfDaysIn(year)
    return jaardag - numberOfDay(year, month, day)

def remainingNumberOfDayInMonth(year, month, day):
    maanddag = numberOfDaysIn(year, month)
    return maanddag - day  

def dateDiffInDays(yearA, monthA, dayA, yearB, monthB, dayB):
    dagA = numberOfDay(yearA, monthA, dayA, 1900)
    dagB = numberOfDay(yearB, monthB, dayB, 1900)
    ret = dagB - dagA

    return ret

def before(yearA, monthA, dayA, yearB, monthB, dayB):
    if dateDiffInDays(yearA, monthA, dayA, yearB, monthB, dayB)>0:
        return 1
    else:
        if dateDiffInDays(yearA, monthA, dayA, yearB, monthB, dayB) == 0:
            return 0
     
    return -1

def after(yearA, monthA, dayA, yearB, monthB, dayB):
    if dateDiffInDays(yearA, monthA, dayA, yearB, monthB, dayB)>0:
        return -1   
    else:
        if dateDiffInDays(yearA, monthA, dayA, yearB, monthB, dayB) == 0:
            return 0 
    return 1

def makePosDays(days, sinceYear):
    retDays = days
    retYear = sinceYear
    if days < 0:
        #get number of days of lst year                
        while retDays < 0:
            retYear -= 1
            retDays = retDays + numberOfDaysIn(retYear)
    else:
        #aantal dagen bij 1/1 geteld -> retDays+1 zodat we in juiste jaar vallen.
        retDays += 1        
        while retDays > numberOfDaysIn(retYear):
            retDays = retDays - numberOfDaysIn(retYear)
            retYear += 1
        #corrigeren voor extra dag        
        retDays -= 1
    return retDays, retYear

def date(days, sinceYear):
    #dag op days afstand van 1/1/sinceYear
    year = 0
    month = 0
    day = 0
    #we zorgen er eerst voor dat we beginnen met pos aantal dagen < jaar    
    days, sinceYear = makePosDays(days, sinceYear)
    #aantal dagen bij 1/1 geteld -> days +1
    days = days + 1
    year = sinceYear        
    lengteJaar = numberOfDaysIn(sinceYear)
    #binnen zelfde jaar
    if days <= lengteJaar:
        i=1
        while i<=12:
            if days > numberOfDaysIn(year, i):
                days -= numberOfDaysIn(year, i)
            else:
                month = i
                day = days
                return year, month, day
            i+=1
    return year, month, day

def add(year, month, day, days):
    ##index van dag sinds 1-1-1900
    dayIndex = numberOfDay(year, month, day, year)    
    ##aantal dagen erbij tellen
    dayIndex += days
    ##nieuwe datum terughalen (maar -1 want date neem dag op days afstand van 1/1)
    retYear, retMonth, retDay = date(dayIndex - 1, year)
    return retYear, retMonth, retDay

def birthdayAlreadyPassedThisYear(year, month, day):
    currentYear, currentMonth, currentDay = today()
    if  numberOfDay(year, month, day,1900) < numberOfDay(currentYear, currentMonth, currentDay,1900):
        if before(currentYear, month, day, currentYear, currentMonth, currentDay) >= 0:
            return True
    return False

def age(year, month, day):
    currentYear, currentMonth, currentDay = today()
    if  numberOfDay(year, month, day,1900) < numberOfDay(currentYear, currentMonth, currentDay,1900):
        if birthdayAlreadyPassedThisYear(year, month, day):
            return currentYear - year
        else:
            return currentYear - year - 1
    else:
        return 0
    return NotImplemented