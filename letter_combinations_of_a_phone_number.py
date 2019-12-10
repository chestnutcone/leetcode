# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:15:21 2019

@author: Oliver
"""


"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        word_dict = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}
        def concat_strs(ls, letter_ls):
            return ['{}{}'.format(s,letter) for letter in letter_ls for s in ls]
        
        digit_size = len(digits)
        if digits:
            if digit_size == 1:
                return word_dict[digits[0]]
            else:
                answer = concat_strs(word_dict[digits[0]], word_dict[digits[1]])
                for i in digits[2:]:
                    answer = concat_strs(answer, word_dict[i])
                return answer
        else:
            return []