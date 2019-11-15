# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:50:48 2019

@author: Himanshu
"""
from collections import Counter
words = "if there was there was but if there was not there was not".split()
print(words)
counts = Counter(words)
print(counts.most_common(3))
for i in counts:
    print(counts[i])
#print(counts)
# List comprehension
#test = sum([i * i for i in range(1, 10000001)])
#print(test)

# Generator
test = sum((i * i for i in range(1, 100001)))
#print(test)

class Solution(object):
    """
    Explanation:
    This problem is the Fibonacci sequence in disguise
    You have a recurrence relationship that is
    S_i = S_(i-1) + S_(i-2)
    and you have to solve it without blowing the stack,
    i.e. save the solution to previous sub problems
    O(n) Time
    O(n) Space
    """
  
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        steps = [0 for _ in range(n + 1)]
       # breakpoint()
        for num in (0,1,2):
            steps[num] = num
            
        for num in range(3, n+1):
            steps[num] = steps[num-1] + steps[num-2]

        return steps[n]
    
r = Solution()
res = r.climbStairs(5)
#print (res)