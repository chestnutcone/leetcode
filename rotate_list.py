# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:22:09 2020

@author: Oliver
"""
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head:
            all_num = []
            start = head

            while start:
                all_num.append(start.val)
                start = start.next
            # rotate
            start = head
            counter = (len(all_num)-k) % len(all_num)
            while start:
                if counter>= len(all_num):
                    counter = 0

                start.val = all_num[counter]
                counter += 1
                start = start.next
                
        return head