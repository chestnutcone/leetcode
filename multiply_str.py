# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:06:59 2019

@author: Oliver
"""
"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num2 = num2[::-1]
        num1 = num1[::-1]
        carry = 0
        result = {}
        for i in range(len(num2)):
            for j in range(len(num1)):
                pos = i+j
                placeholder = result.get(pos)

                dig2 = ord(num2[i])-48
                dig1 = ord(num1[j])-48
                mul = dig1*dig2
                carry = mul // 10
                add = mul%10
                if placeholder:
                    placeholder.append(add)
                else:
                    result[pos] = [add]

                if carry:
                    next_placeholder = result.get(pos+1)
                    if next_placeholder:
                        next_placeholder.append(carry)
                    else:
                        result[pos+1] = [carry]

        answer = ""
        last_dig = None
        for ans in range(len(result)):
            add = sum(result[ans])
            carry = add//10
            if carry:
                next_dig = result.get(ans+1)
                if next_dig:
                    next_dig.append(carry)
                else:
                    last_dig = carry

            answer += "{}".format(add%10)
        if last_dig:
            answer += "{}".format(last_dig)
        answer = answer[::-1]
        return answer