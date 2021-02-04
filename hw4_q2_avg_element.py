# CS362_Winter21
# HW4
# Program: hw4_q2_avg_element.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that calculates the average of elements in a list.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_q2_avg_element.py
###########################################################################

def cal_average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

try:
    arr = [1, 2, 3, 4]
except Exception as e:
    print("Invalid input! :", e)
else:
    print("The average of elements in a list: ", round(cal_average(arr), 2))
print()