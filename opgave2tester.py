from unittest import TestCase
from opgave2opl import *

class opgave2tester(TestCase):

    def testSplit(self):
        self.assertEqual(['appels', 'en', 'peren'], split('appels en peren', ' '))
        self.assertEqual(['appels', 'en', 'peren'], split(' appels en peren ', ' '))
        self.assertEqual(['appels', 'peren'], split(' appels & peren&', '&'))
        self.assertEqual(['appels', 'peren'], split('& &appels & peren& ', '&'))
        self.assertEqual(['appels en peren'], split('& &appels en peren& &', '&'))
        self.assertEqual(['appels en peren', 'bananen'], split('& &appels en peren& bananen&', '&'))

    def testIsDigit(self):
        self.assertEqual(True, isDigit('9'))
        self.assertEqual(False, isDigit('a'))

    def testToUpper(self):
        self.assertEqual('123ABCXYZ#@&', toUpper('123abcXYZ#@&'))

    def testToLower(self):
        self.assertEqual('123abcxyz#@&', toLower('123abcXYZ#@&'))

    def testIsAlpha(self):
        self.assertEqual(True, isAlpha('a'))
        self.assertEqual(True, isAlpha('A'))
        self.assertEqual(False, isAlpha('9'))
        self.assertEqual(False, isAlpha('%'))

    def testIsGeheel(self):
        self.assertEqual(True, isGeheel('314'))
        self.assertEqual(True, isGeheel('-314'))
        self.assertEqual(False, isGeheel('-3.14'))
        self.assertEqual(True, isGeheel('+  314'))
        self.assertEqual(False, isGeheel('@  314'))

    def testTrim(self):
        self.assertEqual('abc', trim(' \t\r\nabc \t\r\n'))
        self.assertEqual('a', trim(' \t\r\na \t\r\n'))
        self.assertEqual('', trim(' \t\r\n \t\r\n'))
        self.assertEqual('a\rb', trim(' \t\ra\rb \t\r\n'))

    def testCountDigit(self):
        self.assertEqual(9, countDigit('Op woensdag 16/11/2016 vindt het 2de werkcollege plaats.'))

    def testCountAlpha(self):
        self.assertEqual(37, countAlpha('Op woensdag 16/11/2016 vindt het 2de werkcollege plaats.'))

    def testGetValidTransaction(self):
        self.assertEqual(('D',400), getValidTransaction('D 400'))
        self.assertEqual(('D',0), getValidTransaction('X 100'))
        self.assertEqual(('D',0), getValidTransaction('d100'))
        self.assertEqual(('D',0), getValidTransaction('W -200'))
        self.assertEqual(('D',0), getValidTransaction('D 100 150'))

    def testSpecial(self):
        self.assertEqual(9999, special(9,4))
        self.assertEqual(9, special(9,1))
        self.assertEqual(0, special(9,0))

    def testSpecialFaculteit(self):
        self.assertEqual(11106, specialFaculteit(9,4))
        self.assertEqual(9, specialFaculteit(9,1))
        self.assertEqual(0, specialFaculteit(9,0))

    def testMove(self):
        self.assertEqual((0,0), move(0,0, 'U', 0))
        self.assertEqual((0,1), move(0,0, 'U', 1))
        self.assertEqual((0,-1), move(0,0, 'D', 1))
        self.assertEqual((-1,0), move(0,0, 'L', 1))
        self.assertEqual((1,0), move(0,0, 'R', 1))

    def testHasUpper(self):
        self.assertEqual(False, hasUpper('qsdfq'))
        self.assertEqual(True, hasUpper('Qmlkjml'))

    def testHasLower(self):
        self.assertEqual(False, hasLower('AERAEZ'))
        self.assertEqual(True, hasLower('321321a'))

    def testHasDigit(self):
        self.assertEqual(False, hasDigit('AERAEZ'))
        self.assertEqual(True, hasDigit('321321a'))

    def testHasSpecialleke(self):
        self.assertEqual(False, hasSpecialleke('AZEARZEA'))
        self.assertEqual(True, hasSpecialleke('QSDFQSD$'))

    def testValidatePassword(self):
        self.assertEqual(True, isValidPassword('ABd1234@1'))
        self.assertEqual(False, isValidPassword('a F1#'))
        self.assertEqual(False, isValidPassword('12345678'))
        self.assertEqual(True, isValidPassword('aB$1234'))
        self.assertEqual(False, isValidPassword('9z5D@'))
        self.assertEqual(True, isValidPassword('1a2B3#'))
        self.assertEqual(True, isValidPassword('Abcd1234#xyz'))
        self.assertEqual(False, isValidPassword('a$1d6Tt33xsq#9'))