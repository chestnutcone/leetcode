# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:58:58 2019

@author: Oliver
"""

"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <3:
            return 0
        l = None
        for i in range(len(height)):
            # find l
            if height[i]:
                l=i
                break
        rev_height = height[::-1]
        rev_l = None
        for i in range(len(height)):
            if rev_height[i]:
                rev_l=i
                break

        def find_water(start, arr):
            accum = 0
            total_accum = 0
            l = arr[start]
            for i in range(start+1, len(arr)):
                if arr[i] >= l:
                    # found bound
                    total_accum += accum
                    accum = 0
                    l = arr[i]

                accum += l - arr[i]

            return total_accum
        peak = height.index(max(height))
        return find_water(l, height[:peak+1])+find_water(rev_l, rev_height[:len(height)-peak])