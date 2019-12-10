# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:24:43 2019

@author: Oliver
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        cutoff = nums[0]
        vert = 0
        search = False
        for i, num in enumerate(nums):
            if num<cutoff:
                vert = i
                search = True
                break
        # print('vert', vert)
        if search:
            if target < cutoff:
                # print('target small')
                search_half = nums[vert:]
            else:
                search_half = nums[:vert]
        else:
            search_half = nums
        # print('search half', search_half)
        def binary_search(arr, val):
            idx = -1
            mid = len(arr) //2
            l,r = 0, len(arr)
            while l<r:
                if target < arr[mid]:
                    r = mid
                elif target > arr[mid]:
                    l = mid +1
                else:
                    idx = mid
                    break
                mid = (l+r) // 2
            # print(idx,mid)
            return idx
        idx = binary_search(search_half, target)
        if target < cutoff and idx != -1:
            idx += vert
        return idx
