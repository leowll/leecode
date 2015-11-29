# -*- coding: utf-8 -*-
__author__ = 'leo'
"""
    package.module
    ~~~~~~~~~~~~~~

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

    :copyright: (c) YEAR by AUTHOR.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

line = raw_input()
sum_value = raw_input()

nums = line.split(' ')
num_integers = map(int, nums)
sum_integer = int(sum_value)
array_length = len(num_integers)

other_array = [sum_integer - e for e in num_integers]
print other_array
for i in range(0, array_length):
    found = False
    for j in range(0, array_length):
        if num_integers[i] == other_array[j]:
            found = True
            print 'index1={0},index2={1}'.format(i, j)
            break
    if found:
        break
