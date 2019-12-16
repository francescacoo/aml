# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:07:07 2019

@author: francescacoo
"""

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

n=5
    
for i in range(n):   
    print(fib(i))
        


