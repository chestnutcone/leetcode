# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:25:48 2019

@author: Oliver
"""

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r,mid = 0,len(nums), len(nums)//2
        closest = -1
        while l<r:
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid
            else:
                r = mid
                closest =mid
            mid = (r+l)//2

        if closest == -1:
            return [-1,-1]
        idx = [closest]
        for i in range(l+1, len(nums)):
            if nums[i] != target:
                idx.append(i-1)
                return idx
        try:
            if nums[-1] == target:
                idx.append(i)
        except:
            idx.append(idx[0])

        return idx