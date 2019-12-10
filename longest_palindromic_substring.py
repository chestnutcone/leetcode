# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:05:03 2019

@author: Oliver
"""


"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def search_pali(s, odd=True):
            str_size = len(s)
            max_str = ''
            for i in range(str_size):
                if odd:
                    l = i-1
                else:
                    l = i
                r = i+1

                temp_str = ''
                while l>=0 and r <str_size and s[l] == s[r]:
                    l -= 1
                    r += 1
                temp_str = s[l+1:r]

                if len(temp_str) > len(max_str):
                    max_str = temp_str
            return max_str
        odd_str = search_pali(s)
        even_str = search_pali(s, odd=False)
        if len(odd_str) > len(even_str):
            return odd_str
        else:
            return even_str
