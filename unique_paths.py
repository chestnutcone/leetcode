# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:18:26 2020

@author: Oliver
"""

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28
"""
def uniquePaths(m,n):
        
    def findPaths(m,n,memo):
        if (m,n) in memo:
            return memo[(m,n)]
        
        if m<2 or n<2:
            if (m<1 or n<1):
                memo[(m,n)] = None
            else:
                memo[(m,n)] = 1
        else:
            if m==2 and n==2:
                # base case
                memo[(m,n)] = 2   
            elif m == n:
                # need double of left
                memo[(m,n)] = findPaths(m,n-1, memo)*2
            elif n == 2:
                # left most column
                memo[(m,n)] = m
            elif m == 2:
                memo[(m,n)] = n
            else:
                memo[(m,n)] = findPaths(m-1,n, memo) + findPaths(m,n-1, memo)
        # print(memo)
        # raise Exception
        return memo[(m,n)]
    return findPaths(m,n,{})