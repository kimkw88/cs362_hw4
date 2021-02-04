# CS362_Winter21
# HW4
# Program: hw4_tests_q2_avg_element.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_tests_q2_avg_element.py
###########################################################################

import unittest
import hw4_q2_avg_element as q2

class AverageTests(unittest.TestCase):
    
    # Ex_case 1)
    # if length of arr >= 0 ----> (4 > 0) ---------- ok
    # if length of arr >= 100 --> (4 > 100) -------- FAIL
    def test_greater_equal1(self):
        self.assertGreaterEqual(len(q2.arr), 0)
    def test_greater_equal2(self):
        self.assertGreaterEqual(len(q2.arr), 100)

    # Ex_case 2)
    # if cal_average([1,2,3,4]) --> ( 2.5 == 2.5) -- ok
    # if cal_average([1,2,3,4]) --> ( 2.5 != 2) ---- FAIL 
    def test_equal1(self):
        self.assertEqual(q2.cal_average([1,2,3,4]), 2.5)
    def test_equal2(self):
        self.assertEqual(q2.cal_average([1,2,3,4]), 2)

    # Ex_case 3)
    # if [1,2,3,4] == [1,3,2,4]  --> (both has the same) --- ok
    # if [1,2,3,4] == [5,2,3,4]  --> (different 1 and 5) --- FAIL 
    def test_count_equal1(self):
        self.assertCountEqual(q2.arr, [1, 3, 2 ,4])
    def test_count_equal2(self):
        self.assertCountEqual(q2.arr, [5, 2, 3 ,4])

if __name__ == '__main__':
    unittest.main(verbosity=2)