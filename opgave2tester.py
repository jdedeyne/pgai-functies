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
