# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:43:52 2019

@author: Himanshu
"""

def compress(s):
    l = len(s)
    if l==0:
        return ''
    elif l==1:
        return s+'1'
    
    i = 1
    cnt = 1
    res = ""
    
    while i<l:
        if s[i]==s[i-1]:
            cnt+=1
        else:
            res = res+s[i-1]+str(cnt)
            cnt = 1
        i+=1
    res = res+s[i-1]+str(cnt)
    return res

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)