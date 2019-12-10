# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:23:24 2019

@author: Oliver
"""

"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        temp_ls = []
        err_ls = []
        last_err = 0
        max_valid = 0
        temp_valid = 0

        for i, val in enumerate(s):
    #        print(temp_ls)
            if val == '(':
                temp_ls.append(i)
            else:
                try:
                    temp_ls.pop()
                except IndexError:
                    err_ls.append(i)
        err_ls.extend(temp_ls)
        err_ls.sort()
        if err_ls:
            for e in range(len(err_ls)-1):
                temp_valid = err_ls[e+1] - err_ls[e] -1
                if temp_valid > max_valid:
                    max_valid = temp_valid
            if len(s)-err_ls[-1]-1 > max_valid:
                max_valid = len(s)-err_ls[-1]-1
            if err_ls[0] > max_valid:
                max_valid = err_ls[0]
        else:
            return len(s)

        return max_valid