# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:30:38 2019

@author: Oliver
"""

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

THIS IS NOT MY SOLUTION. THIS IS A DFS, AND EACH ROUND, THE NEXT CANDIDATE
IS LIMITED TO ONLY NUMS AFTER CANDIDATE TO GENERATE UNIQUE COMBINATIONS
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, val, path, res):
            if val < 0:
                return
            elif val == 0:
                res.append(path)
                return
            else:
                for i in range(index, len(candidates)):
                    dfs(i, val-candidates[i], path+[candidates[i]], res)

        dfs(0,target,[],res)
        return res