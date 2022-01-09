from unittest import TestCase
from opgave3opl import *

class opgave3tester(TestCase):

    def testSubstr(self):
        self.assertEqual('', substr('voetbalveld', 0, 0))
        self.assertEqual('', substr('voetbalveld', 0, -1))
        self.assertEqual('', substr('voetbalveld', -11, -1))
        self.assertEqual('', substr('voetbalveld', -15, -1))
        self.assertEqual('', substr('voetbalveld', 11, 1))
        self.assertEqual('voet', substr('voetbalveld', -11, 4))
        self.assertEqual('veld', substr('voetbalveld', 11, -4))
        self.assertEqual('voetbalveld', substr('voetbalveld', -11, 12))

        self.assertEqual('voet', substr('voetbalveld', 0, 4))
        self.assertEqual('bal' , substr('voetbalveld', 4, 3))
        self.assertEqual('bal', substr('voetbalveld', 7, -3))
        self.assertEqual('bal', substr('voetbalveld', -7, 3))
        self.assertEqual('bal', substr('voetbalveld', -4, -3))
        self.assertEqual('veld', substr('voetbalveld', 7, 4))

    def testReverse(self):
        self.assertEqual('',reverse(''))
        self.assertEqual('lab', reverse('bal'))

    def testIsPalindrome(self):
        self.assertEqual(False,isPalindrome(''))
        self.assertEqual(True, isPalindrome('aibohphobia'))
        self.assertEqual(True, isPalindrome('abba'))
        self.assertEqual(True, isPalindrome('aboba'))
        self.assertEqual(False, isPalindrome('abka'))

    def testFind(self):
        self.assertEqual(4,find('bal', 'voetbalbal'))
        self.assertEqual(4, find('bal', 'voetbalbal', 4))
        self.assertEqual(7, find('bal', 'voetbalbal', 5))
        self.assertEqual(0, find('haha', 'hahaha'))
        self.assertEqual(2, find('haha', 'hahaha', 1))
        self.assertEqual(-1, find('haha', 'hahaha', 3))
        self.assertEqual(-1, find('haha', 'ha'))

    def testFindAll(self):
        self.assertEqual([0, 2, 4],findAll('ha', 'hahaha'))
        self.assertEqual([0, 2], findAll('haha', 'hahaha'))
        # geen overlap -> self.assertEqual([0], findAll('haha', 'hahaha'))
        self.assertEqual([2, 4], findAll('ha', 'hahaha', 1))
        # geen overlap -> self.assertEqual([6], findAll('haha', 'hahahihahahahihiha', 1))
        self.assertEqual([6, 8], findAll('haha', 'hahahihahahahihiha', 1))
        # geen overlap -> self.assertEqual([0, 6], findAll('haha', 'hahahihahahahihiha'))
        self.assertEqual([0, 6, 8], findAll('haha', 'hahahihahahahihiha'))

    def testReplace(self):
        self.assertEqual('voetloblob', replace('bal', 'lob', 'voetbalbal'))
        self.assertEqual('voet', replace('bal', '', 'voetbalbal'))
        self.assertEqual('balbal', replace('voet', '', 'voetbalbal'))
        self.assertEqual('voetbalbal', replace('sok', 'lob', 'voetbalbal'))
        self.assertEqual('hohohoho', replace('haha', 'hoho', 'hahaha'))
        # geen overlap -> self.assertEqual('hohoha', replace('haha', 'hoho', 'hahaha'))'

    def testInDutchThreeDigit(self):
        self.assertEqual('nul', threeDigitInDutch(0))
        self.assertEqual('negen', threeDigitInDutch(9))
        self.assertEqual('achttien', threeDigitInDutch(18))
        self.assertEqual('zevenenvijftig', threeDigitInDutch(57))
        self.assertEqual('tweeëntwintig', threeDigitInDutch(22))
        self.assertEqual('honderdtien', threeDigitInDutch(110))
        self.assertEqual('driehonderdvijftien', threeDigitInDutch(315))
        self.assertEqual('driehonderddrieëndertig', threeDigitInDutch(333))
        self.assertEqual('driehonderd', threeDigitInDutch(300))
        self.assertEqual('driehonderdenzeven', threeDigitInDutch(307))
        
    def testInDutch(self):
        self.assertEqual('zevenhonderdeenentachtig miljoen vierhonderdtweeënvijftigduizend driehonderdeenentwintig', inDutch(781452321))
        self.assertEqual('een miljoen duizend een', inDutch(1001001))

    def testDecompose(self):
        self.assertEqual([1, 0, 2, 0, 3], decompose(30201))
