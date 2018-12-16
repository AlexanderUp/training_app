# encoding: utf-8
# unittest for dayCalc kivy app

# only validate function tested!

# python3 -m unittest -v dayCalc_unittests.py

import unittest
import sys

try:
    from dayCalc_logic import DayCalcDateValidation
except ImportError as err:
    print('Can\'t import Logic!')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Import successfull')

# all tests fail, should be refactored
# problem is in hard connection with MainLayout class in dayCalc app
class dayCalcTest(unittest.TestCase):

    def test(self):
        t = DayCalcDateValidation()
        res = t.validate([2012, 2, 28])
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
