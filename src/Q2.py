# -*- coding: utf-8 -*-
__author__ = 'leo'
"""
    package.module
    ~~~~~~~~~~~~~~

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    :copyright: (c) YEAR by AUTHOR.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        increment = 0
        result_list = []
        while l1 is not None:
            sum_value = (l1.val + l2.val + increment)
            if (sum_value / 10) >= 1:
                increment = 1
            else:
                increment = 0
            result_list.append(sum_value % 10)
            l1 = l1.next
            l2 = l2.next
        return result_list


if __name__ == '__main__':

    line1 = raw_input()
    line2 = raw_input()

    val_list1 = [int(e) for e in line1.split(" ")]
    val_list2 = [int(e) for e in line2.split(" ")]

    list_length = len(val_list1)

    l1 = []
    l2 = []

    for i in range(0, list_length):
        l1.append(ListNode(val_list1[i]))
        l2.append(ListNode(val_list2[i]))

    for i in range(0, list_length - 1):
        l1[i].next = l1[i + 1]
        l2[i].next = l2[i + 1]

    s = Solution()
    result = s.addTwoNumbers(l1[0], l2[0])
    print result
