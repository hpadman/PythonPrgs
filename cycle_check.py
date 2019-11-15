# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:13:54 2019

@author: Himanshu
"""

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        

def cycle_check(Node):
    fast,slow = Node,Node
    while fast and fast.next:
        fast = fast.next
        if fast==slow:
            return True
        fast = fast.next
        slow=slow.next
        
    return False

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z

class TestCycle(object):
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
    
        print("Success")
    
t = TestCycle()
t.test(cycle_check)
        