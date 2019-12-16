# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:49:25 2019

@author: francescacoo
"""


import unittest

import task1

class Testing(unittest.TestCase):
    def test_series_2(self):
        print('\nTest Series 2')
        wanted_result = 1
        test_result = task1.fib(2)
        self.assertEqual(wanted_result,test_result)

    def test_series_5(self):
        print('\nTest Series 2')
        wanted_result = 5
        test_result = task1.fib(5)
        self.assertEqual(wanted_result,test_result)
        
    def test_series_12(self):
        print('\nTest Series 2')
        wanted_result = 144
        test_result = task1.fib(12)
        self.assertEqual(wanted_result,test_result)

if __name__ == '__main__' : unittest.main()