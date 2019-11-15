# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:33:40 2019

@author: Himanshu
"""

def cyclic(arr1,k):
    res = [None]*len(arr1)
    for i in range(0,len(arr1)):
        newpos = (i+k)%len(arr1)
        res[newpos]=arr1[i]
    return res

test = cyclic([7,2,8,3,5,6],2)
print(test)
    