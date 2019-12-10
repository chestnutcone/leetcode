# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:20:07 2019

@author: Oliver
"""

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        lists = [x for x in lists if x]
        if len(lists)==0:
            return None
        elif len(lists)==1:
            return lists[0]
        all_nums = []
        for l in lists:
            while l:
                all_nums.append(l.val)
                l = l.next
        
        all_nums.sort()
        head = cur = ListNode(0)
        for i in range(len(all_nums)-1):
            cur.val = all_nums[i]
            cur.next = ListNode(None)
            cur = cur.next
        cur.val = all_nums[-1]
        return head
            