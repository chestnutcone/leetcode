# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:18:52 2019

@author: Oliver
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
    
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate permutations
        if n == 0:
            return ['']
        if n == 1:
            return ['()']

        all_prev = {i:self.generateParenthesis(i) for i in range(1,n)}

        permu = set()
        for i in range(1,n):
            # gen all possible

            forward = all_prev[i]
            rev = all_prev[n-i]

            permu.update({'{}{}'.format(x,y) for x in forward for y in rev})
            permu.update({'{}{}'.format(y,x) for y in forward for x in rev})

        prev_run = all_prev[n-1]
        permu.update({'({})'.format(x) for x in prev_run})

        permu = list(permu)
        return permu