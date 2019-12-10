# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:21:45 2019

@author: Oliver
"""

"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero


Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of 
this problem, assume that your function returns 231 − 1 when the division result overflows.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        neg = 1 if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else -1
        LIM = 2147483648
        divisor = abs(divisor)
        dividend = abs(dividend)

        if divisor == 1:
            result = dividend*neg
            if result > LIM-1 or result < -LIM:
                return LIM-1
            else:
                return dividend*neg

        divisor_queue = [(1,divisor)]
        i = 0
        counter = 0
        while dividend >=0 and i>=0:
            div = divisor_queue[i][1]
            mul = divisor_queue[i][0]
            if div > dividend:
                i -= 1
                continue
            dividend -= div
            counter += mul
            i += 1
            divisor_queue.append((mul+mul, div+div))

        return counter*neg