# CS362_Winter21
# HW4
# Program: hw4_tests_q1_volume_cube.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_tests_q1_volume_cube.py
###########################################################################

import sys
import unittest
import hw4_q1_volume_cube as q1

class VolumeTests(unittest.TestCase):
    
    # Ex_case 1)
    # if volume > 0   --> (35.397 > 0) --------- ok
    # if volume > 100 --> (35.397 > 100) ------- FAIL
    def test_greater1(self):
        self.assertGreater(q1.cal_volume(3.3), 0)
    def test_greater2(self):
        self.assertGreater(q1.cal_volume(3.3), 100)

    # Ex_case 2)
    # if length == 3.3 --> (3.3 == float) ----- ok
    # if length == 3.3 --> (3.3 == int) ------- FAIL 
    def test_type_true1(self):
        self.assertTrue(type(q1.cal_volume(3.3)) is float)
    def test_type_true2(self):
        self.assertTrue(type(q1.cal_volume(3.3)) is int)

    # Ex_case 3)
    # if volume < maxsize --> (35.397 < 9223372036854775295) -- ok
    # if volume < 0 --------> (35.397 < 0) -------------------- FAIL
    def test_less1(self):
        self.assertLess(q1.cal_volume(3.3), sys.maxsize)
    def test_less2(self):
        self.assertLess(q1.cal_volume(3.3), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)