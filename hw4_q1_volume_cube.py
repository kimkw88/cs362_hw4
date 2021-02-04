# CS362_Winter21
# HW4
# Program: hw4_q1_volume_cube.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that calculates the volume of a cube.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_q1_volume_cube.py
###########################################################################

def cal_volume(length):
    return length * length * length
    
try:
    length = 3.3
    assert length > 0
except AssertionError:
    print("The length should be a positive!")  
except TypeError:
    print("Input type error!")      
except Exception as e:
    print("Invalid input! :", e)
else:
    print("The volume of the cube: ", round(cal_volume(length), 2))
print()