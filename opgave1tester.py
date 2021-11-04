from unittest import TestCase
from opgave1opl import *
from math import *

class opgave1tester(TestCase):

    def testGgd(self):
        self.assertEqual(13, ggd(273, 1430))
        self.assertEqual(3, ggd(15, 12))
       

    def testKeerOm(self):
        self.assertEqual(-43021, keerOm(-1203400))

    def testFaculteit(self):
        self.assertEqual(5040, faculteit(7))
        self.assertEqual(1, faculteit(0))

    def testGemiddelde(self):
        self.assertEqual(1.5, gemiddelde([0, 1, 2, 3]))
        self.assertEqual(0, gemiddelde([-3, -1, 1, 3, 0]))
        self.assertEqual(True, isnan(gemiddelde([])))

    def testgrootstePriemKleinerDanOfGelijkAan(self):
        self.assertEqual(101, grootstePriemKleinerDanOfGelijkAan(102))
        self.assertEqual(101, grootstePriemKleinerDanOfGelijkAan(101))
        self.assertEqual(97, grootstePriemKleinerDanOfGelijkAan(100))
        self.assertEqual(2, grootstePriemKleinerDanOfGelijkAan(2))
        self.assertEqual(True, isnan(grootstePriemKleinerDanOfGelijkAan(1)))
        self.assertEqual(True, isnan(grootstePriemKleinerDanOfGelijkAan(0)))
        self.assertEqual(True, isnan(grootstePriemKleinerDanOfGelijkAan(-1)))

    def testVariatie(self):
        self.assertEqual(7, variatie(7, 1))
        self.assertEqual(5040, variatie(7, 6))
        self.assertEqual(1500000000, variatie(1500000000, 1))
        self.assertEqual(0, variatie(6, 7))
        self.assertEqual(0, variatie(-7, -6))
        self.assertEqual(0, variatie(-7, 6))
        self.assertEqual(0, variatie(7, -6))
        self.assertEqual(1, variatie(0, 0)) 
        