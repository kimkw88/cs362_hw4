# CS362_Winter21
# HW4
# Program: hw4_q3_gen_full_name.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that generates a full name when you provide the first and 
#   last name as inputs.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_q3_gen_full_name.py
###########################################################################

def gen_full_name(fname, lname):
    if fname.isalpha() == False or lname.isalpha() == False:
        return
    else:
        return fname + " " + lname

try:
    fname = input("Enter the first name: ").strip()
    lname = input("Enter the last name: ").strip()
except TypeError:
    print("Input type error!")
except Exception as e:
    print("Invalid input! :", e)
else:
    print("Full name: {}".format(gen_full_name(fname, lname)) + "\n")