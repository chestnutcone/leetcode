# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:11:26 2019

@author: Oliver
"""

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not any(nums):
            if nums and len(nums) >=3:
                return [[0,0,0]]
            else:
                return []
        nums.sort()
        result = []

        nums_len = len(nums)

        for i in range(nums_len-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            l,r = i+1, nums_len-1

            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    # result
                    result.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif total<0:
                    # needs larger
                    l += 1
                else:
                    # needs smaller
                    r -= 1
        return result
