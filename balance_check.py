# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:17:36 2019

@author: Himanshu
"""

('[](){([[[]]])}')

def balance_check(s):
    chars = []
    matches = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in matches:
            if chars.pop()!=matches[c]:
                return False
        else:
            chars.append(c)
    return True

test = balance_check('[](){([[[]]])}')
print(test)