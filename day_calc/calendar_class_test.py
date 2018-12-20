# encoding: utf-8
# unittest for dayCalc kivy app

# only validate function tested!

# python3 -m unittest -v calendar_class_test.py

print('*' * 75)

import unittest
import sys

try:
    from calendar_class import LeapCalendar
except ImportError as err:
    print('Can\'t import LeapCalendar!')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('LeapCalendar module imported successfully\n')

t = LeapCalendar()

class dayCalcTest(unittest.TestCase):

    # date validation tests
    def test1(self):
        # t = LeapCalendar()
        res = t.validate((2012, 2, 28))
        self.assertEqual(res, True)

    def test2(self):
        # t = LeapCalendar()
        res = t.validate((2012, 3, 1))
        self.assertEqual(res, True)

    def test3(self):
        # t = LeapCalendar()
        res = t.validate((2012, 6, 30))
        self.assertEqual(res, True)

    def test4(self):
        # t = LeapCalendar()
        res = t.validate((2012, 8, 8))
        self.assertEqual(res, True)

    def test5(self):
        # t = LeapCalendar()
        res = t.validate((1999, 12, 31))
        self.assertEqual(res, True)

    def test6(self):
        # t = LeapCalendar()
        res = t.validate((2012, 1, 1))
        self.assertEqual(res, True)

    def test7(self):
        # t = LeapCalendar()
        res = t.validate((2011, 6, 30))
        self.assertEqual(res, True)

    def test8(self):
        # t = LeapCalendar()
        res = t.validate((2011, 1, 1))
        self.assertEqual(res, True)

    def test9(self):
        # t = LeapCalendar()
        res = t.validate((1900, 1, 1))
        self.assertEqual(res, True)

    def test10(self):
        # t = LeapCalendar()
        res = t.validate((2012, 2, 29))
        self.assertEqual(res, True)

    def test11(self):
        # t = LeapCalendar()
        res = t.validate((2013, 2, 29))
        self.assertEqual(res, False)

    def test12(self):
        # t = LeapCalendar()
        res = t.validate((2018, 10, 45))
        self.assertEqual(res, False)

    def test13(self):
        # t = LeapCalendar()
        res = t.validate((2018, 15, 12))
        self.assertEqual(res, False)

    def test14(self):
        # t = LeapCalendar()
        res = t.validate((2011, -12, 2))
        self.assertEqual(res, False)

    # days between dates tests
    def test15(self):
        # t = LeapCalendar()
        res = t.daysBetweenDates(2012, 1, 1, 2012, 2, 28)
        self.assertEqual(res, 58)

    def test16(self):
        # t = LeapCalendar()
        res = t.daysBetweenDates(2012, 1, 1, 2012, 3, 1)
        self.assertEqual(res, 60)

    def test17(self):
        # t = LeapCalendar()
        res = t.daysBetweenDates(2011, 6, 30, 2012, 6, 30)
        self.assertEqual(res, 366)

    def test18(self):
        # t = LeapCalendar()
        res = t.daysBetweenDates(2011, 1, 1, 2012, 8, 8)
        self.assertEqual(res, 585)

    def test19(self):
        # t = LeapCalendar()
        res = t.daysBetweenDates(1900, 1, 1, 1999, 12, 31)
        self.assertEqual(res, 36523)


if __name__ == '__main__':
    unittest.main()
