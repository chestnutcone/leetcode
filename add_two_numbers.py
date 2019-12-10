# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:28:56 2019

@author: Oliver
"""

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_node = ListNode(None)
        first_node = cur_node
        carry = 0
        while l1 or l2:
            if l1 and l2: 
                sum_val = l1.val + l2.val + carry   
            else:
                try:
                    sum_val = l1.val
                except:
                    sum_val = l2.val
                sum_val +=  carry
            if sum_val >9:
                carry = 1
                sum_val -= 10
            else:
                carry = 0   
            try:
                l1 = l1.next
            except:
                l1 = None
            
            try:
                l2 = l2.next
            except:
                l2 = None
            
            if l1 is None and l2 is None:
                if carry == 1:
                    # make extra last node
                    cur_node.val = sum_val
                    cur_node.next = ListNode(1)
                else:
                    # make 
                    cur_node.val = sum_val
            else:
                # do normal
                cur_node.val = sum_val
                cur_node.next = ListNode(None)
                cur_node = cur_node.next

        return first_node