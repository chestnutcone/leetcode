# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:28:06 2020

@author: Oliver
"""

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

def generateMatrix(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    start, lim = 0, n
    num = 1
    while num <= n**2:
        for col in range(start, lim):
            answer[start][col] = num
            num += 1
        for row in range(start+1, lim):
            answer[row][lim-1] = num
            num += 1
        for col in range(lim-2, start-1,-1):
            answer[lim-1][col] = num
            num += 1

        for row in range(lim-2, start, -1):
            answer[row][start] = num
            num += 1
        start += 1
        lim -= 1
    return answer