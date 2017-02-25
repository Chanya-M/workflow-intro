#!/bin/python3

import sys

print('Enter the elements of the array, separated by spaces.')
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr_sum = 0

for i in arr:
    arr_sum += i
    
print(arr_sum)
