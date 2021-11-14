from unittest import TestCase
from opgave4opl import *

class opgave4tester(TestCase):
    def testIsLeapYear(self):
        self.assertEqual(True , isLeapYear(2016))
        self.assertEqual(False, isLeapYear(1997))
        self.assertEqual(True , isLeapYear(1996))
        self.assertEqual(False, isLeapYear(1900))
        self.assertEqual(True, isLeapYear(2000))        

    def testNumberOfDaysIn(self):
        self.assertEqual(28 , numberOfDaysIn(2017, 2))
        self.assertEqual(29 , numberOfDaysIn(2016, 2))
        self.assertEqual(31 , numberOfDaysIn(1996, 7))
        self.assertEqual(365, numberOfDaysIn(1997))
        self.assertEqual(366, numberOfDaysIn(1996))

    def testNumberOfDay(self):
        self.assertEqual(365, numberOfDay(2017, 12, 31))
        self.assertEqual(366, numberOfDay(2016, 12, 31))
        self.assertEqual(1, numberOfDay(2016, 1, 1))
        self.assertEqual(366, numberOfDay(2018, 1, 1, 2017))

    def testDateDiffInDays(self):
        self.assertEqual(0, dateDiffInDays(2017, 1, 1, 2017, 1, 1))
        self.assertEqual(1, dateDiffInDays(2017, 1, 1, 2017, 1, 2))
        self.assertEqual(-90, dateDiffInDays(2016, 3, 31, 2016, 1, 1))
        self.assertEqual(90, dateDiffInDays(2016, 1, 1, 2016, 3, 31))
        self.assertEqual(730, dateDiffInDays(2015, 4, 1, 2017, 3, 31))
        self.assertEqual(-730, dateDiffInDays(2017, 3, 31, 2015, 4, 1))

    def testBeforeAndAfter(self):
        self.assertEqual(1, before(2016, 2, 29, 2016, 3, 31))
        self.assertEqual(-1, before(2017, 3, 31, 2015, 4, 1))
        self.assertEqual(0, before(2017, 3, 31, 2017, 3, 31))
        self.assertEqual(-1, after(2016, 2, 29, 2016, 3, 31))
        self.assertEqual(1, after(2017, 3, 31, 2015, 4, 1))
        self.assertEqual(0, after(2017, 3, 31, 2017, 3, 31))

    def testMakePosDays(self):
        self.assertEqual((0,1980), makePosDays(0,1980))
        self.assertEqual((1,1980), makePosDays(1,1980))
        self.assertEqual((364,1979), makePosDays(-1,1980))
        self.assertEqual((365,2016), makePosDays(-1,2017))
        self.assertEqual((0,1902), makePosDays(365,1901))
        self.assertEqual((1,1902), makePosDays(366,1901))
        self.assertEqual((2,1902), makePosDays(367,1901))
        self.assertEqual((31,2004), makePosDays(365+31,2003))

    def testDate(self):
        self.assertEqual((1901, 1, 1), date(0, 1901))
        self.assertEqual((1901, 2, 14), date(44, 1901))
        self.assertEqual((1902, 2, 14), date(365+44, 1901))
        self.assertEqual((2016, 12, 31), date(-1, 2017))
        self.assertEqual((2015, 3, 19), date(-654, 2017))

    def testAdd(self):        
        self.assertEqual((2000, 2, 2), add(2000, 2, 1, 1))
        self.assertEqual((1999, 2, 2), add(1999, 2, 1, 1))
        self.assertEqual((1999, 2, 4), add(1999, 2, 1, 3))
        self.assertEqual((2000, 3, 2), add(2000, 2, 1, 30))
        self.assertEqual((2002, 2, 1), add(2001, 2, 1, 365))
        self.assertEqual((2001, 2, 1), add(1999, 2, 1, 365 + 366))
        self.assertEqual((2002, 2, 1), add(1999, 2, 1, 365 + 366 + 365))
        self.assertEqual((2003, 2, 1), add(1999, 2, 1, 365 + 366 + 365 + 365))
        self.assertEqual((2004, 2, 1), add(2003, 2, 1, 365))
        self.assertEqual((2004, 11, 30), add(1999, 2, 1, 2129))
        self.assertEqual((1999, 2, 1), add(2004, 11, 30, -2129))
        self.assertEqual((1901, 1, 2), add(1900, 12, 30, 3))
        self.assertEqual((1900, 12, 30), add(1901, 1, 2, -3))
        self.assertEqual((2015, 3, 19), add(2017, 1, 1, -654))
        self.assertEqual((1901, 1, 3), add(1901, 1, 1, 2))
        self.assertEqual((1902, 2, 14), add(1901, 1, 1, 365 + 31 + 13))

    def testBirthdayAlreadyPassedThisYear(self):
        self.assertEqual(True, birthdayAlreadyPassedThisYear(1971, 1, 1)) #fails each jan 1st :-)
        self.assertEqual(False, birthdayAlreadyPassedThisYear(1971, 12, 31))
        self.assertEqual(False, birthdayAlreadyPassedThisYear(2100, 1, 1))

    def testAge(self):
        currentYear, currentMonth, currentDay = today()
        self.assertEqual(0, age(2100, 1, 1))
        self.assertEqual(10, age(currentYear - 10, 1, 1))
        self.assertEqual(9, age(currentYear - 10, 12, 31))