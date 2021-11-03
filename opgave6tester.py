from unittest import TestCase
from opgave6opl import *

class opgave6tester(TestCase):

    def testLine(self):
        self.assertEqual('****', line(4))
        self.assertEqual('   *  *', line(4, False, 3))
        self.assertEqual('+', line(1, True, 0, '+'))
        self.assertEqual(' +- +-', line(3, False, 1, '+-'))
        self.assertEqual('', line(0, False, 0, '+'))

    def testRectangleAndSquare(self):
        self.assertEqual('  +++\r\n  + +\r\n  + +\r\n  +++', rectangle(3, 4, False, 2, '+'))
        self.assertEqual('*', rectangle(1, 1, False))
        self.assertEqual(' --\r\n --', rectangle(2, 2, False, 1, '-'))
        self.assertEqual('  *****', rectangle(5, 1, False, 2))
        self.assertEqual('*\r\n*\r\n*\r\n*\r\n*', rectangle(1, 5, False))
        self.assertEqual(' 88888\r\n 8   8\r\n 8   8\r\n 8   8\r\n 88888', square(5, False, 1, '8'))

    def testParallelogram(self):
        self.assertEqual('    ++++\r\n   +  +\r\n  ++++', parallelogram(4, 3, False, 2, '+'))
        self.assertEqual('      OO\r\n    OO', parallelogram(2, 2, True, 4, 'O', -2))
        self.assertEqual('    OO\r\n      OO', parallelogram(2, 2, True, 4, 'O', 2))
        self.assertEqual('XXX\r\n   X X\r\n      XXX', parallelogram(3, 3, False, 0, 'X', 3))
        self.assertEqual('      XXX\r\n   X X\r\nXXX', parallelogram(3, 3, False, 0, 'X', -3))

    def testRightTriangle(self):
        self.assertEqual('  o\r\n    oo\r\n      ooo\r\n        oooo\r\n          ooooo', triangle(5, True, 2, 'o', 2))
        self.assertEqual('  o\r\n    oo\r\n      o o\r\n        o  o\r\n          ooooo', triangle(5, False, 2, 'o', 2))
        self.assertEqual('      x\r\n     xx\r\n    xxx\r\n   xxxx\r\n  xxxxx', triangle(5, True, 2, 'x', 1, True))
        self.assertEqual('  xxxxx\r\n   xxxx\r\n    xxx\r\n     xx\r\n      x', triangle(5, True, 2, 'x', 1, True, False))
        self.assertEqual('  xxxxx\r\n  x  x\r\n  x x\r\n  xx\r\n  x', triangle(5, False, 2, 'x', 0, False, False))
        self.assertEqual('  xxxxx\r\n  xxxx\r\n  xxx\r\n  xx\r\n  x', triangle(5, True, 2, 'x', 0, True, False))
        self.assertEqual('     *\r\n    * *\r\n   *   *\r\n  *******', triangle(7, False, 2, '*', 0, True, True, False))
        self.assertEqual('     **\r\n    *  *\r\n   *    *\r\n  ********', triangle(8, False, 2, '*', 0, True, True, False))
        self.assertEqual('  *******\r\n   *   *\r\n    * *\r\n     *', triangle(7, False, 2, '*', 0, True, False, False))
        self.assertEqual('  ********\r\n   *    *\r\n    *  *\r\n     **', triangle(8, False, 2, '*', 0, True, False, False))