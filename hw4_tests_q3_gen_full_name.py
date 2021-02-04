# CS362_Winter21
# HW4
# Program: hw4_tests_q3_gen_full_name.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_tests_q3_gen_full_name.py
###########################################################################

import unittest
import hw4_q3_gen_full_name as q3

class NameTests(unittest.TestCase):
    
    # Ex_case 1)
    # if type of the value == str ----> (David == str) ---------- ok
    # if type of the value == int ----> (David == int) ---------- FAIL
    def test_type_equal1(self):
        self.assertEqual(type(q3.gen_full_name(q3.fname, q3.lname)), str)
    def test_type_equal2(self):
        self.assertEqual(type(q3.gen_full_name(q3.fname, q3.lname)), int)

    # Ex_case 2)
    # if the value != None ----> (David != None) ---------- ok
    # if the value == None ----> (""    != None) ---------- FAIL
    def test_is_not_none(self):
        self.assertIsNotNone(q3.gen_full_name(q3.fname, q3.lname))
    def test_is_none(self):
        self.assertIsNone(q3.gen_full_name(q3.fname, q3.lname))

    # Ex_case 3)
    # check if a space is in the container ---> (" " in "David Kim") ------ ok
    # check if Joe is in the container -------> ("Joe" in "David Kim") ---- FAIL
    def test_in_container1(self):
        self.assertIn(" ", q3.gen_full_name(q3.fname, q3.lname))
    def test_in_container2(self):
        self.assertIn("Joe", q3.gen_full_name(q3.fname, q3.lname))


if __name__ == '__main__':
    unittest.main(verbosity=2)