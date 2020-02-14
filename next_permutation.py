# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:25:00 2020

@author: Oliver
"""

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # scan the number from right to left 
    if len(nums) > 1:   
        altered = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                next_big = len(nums) - nums[::-1].index(max(nums[i+1:])) -1
                for j in range(len(nums)-1,i,-1):
                    if nums[j] < nums[next_big] and nums[j] > nums[i]:
                        next_big = j
                nums[i], nums[next_big] = nums[next_big], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                altered = True
                break
        if i == 0 and not altered:
            nums[:] = nums[::-1]