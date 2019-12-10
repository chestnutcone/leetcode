# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:12:38 2019

@author: Oliver
"""

"""Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would 
have exactly one solution.

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        num_size = len(nums)

        lowest_diff = float('Inf')

        for i in range(num_size-2):
            l,r = i+1,num_size-1
            if sum(nums[i:i+3])-target > lowest_diff: break
            while l<r:
                diff = nums[i]+nums[l]+nums[r]-target
                abs_diff= 0-diff if diff < 0 else diff
                if abs_diff < lowest_diff:
                    lowest_diff = abs_diff
                    best_match = nums[i]+nums[l]+nums[r]

                if diff>0:
                    r -= 1
                elif diff<0:
                    l += 1
                else:
                    # closest match already
                    return best_match
        return best_match