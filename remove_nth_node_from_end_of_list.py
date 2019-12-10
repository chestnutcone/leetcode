# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:17:21 2019

@author: Oliver
"""

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first_node = head
        
        ls_len = 0 # zero based
        while head:
            ls_len += 1
            head = head.next
        
        pos = ls_len-n
        
        # if it is the first one
        if pos == 0:
            return first_node.next
        
        counter = 0
        head = first_node
        
        while counter != pos-1:
            head = head.next
            counter += 1

        head.next = head.next.next
        return first_node