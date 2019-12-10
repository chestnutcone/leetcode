# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:20:58 2019

@author: Oliver
"""

"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        if head.next is None:
            return head
        
        all_nums = []
        while head:
            all_nums.append(head.val)
            head = head.next
        
        switched_nums = []
        num_size = len(all_nums)
        for i in range(0, num_size, 2):
            try:
                switched_nums.append(all_nums[i+1])
            except IndexError:
                pass
            switched_nums.append(all_nums[i])
        
        new_head = cur = ListNode(0)
        for i in range(num_size-1):
            cur.val = switched_nums[i]
            cur.next = ListNode(None)
            cur = cur.next
        cur.val = switched_nums[-1]
        
        return new_head
            