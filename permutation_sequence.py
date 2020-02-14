# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:23:22 2020

@author: Oliver
"""

import math
"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Input: n = 3, k = 3
Output: "213"

Input: n = 4, k = 9
Output: "2314"
"""
def getPermutation(self, n: int, k: int) -> str:
    numbers = [str(i) for i in range(1,n+1)]
    # get first number
    result = ''
    start_num = k-1
    for i in range(n,0,-1):
        left_combo = math.factorial(i-1)
        num = start_num // left_combo
        result += numbers.pop(num)
        start_num -= num*left_combo
    return result