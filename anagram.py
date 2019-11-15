# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:44:17 2019

@author: Himanshu
"""

def anagram(s,t):
    # remove whitespaces
    s = s.replace(" ","").lower()
    t = t.replace(" ","").lower()
    
    if not s or not t:
        return False
    
   # if len(s)!= len(t):
    #    return False
    
    total = {}
    for char in s:
        if char in total:
           total[char] += 1
        else:
           total[char] = 1
           
    for char in t:
        if char in total:
           total[char] -= 1
        else:
           return False
           
    for c in total:
        if total[c]!=0:
            return False
    
    return True

from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go',''),False)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')

# Run Tests
t = AnagramTest()
t.test(anagram)