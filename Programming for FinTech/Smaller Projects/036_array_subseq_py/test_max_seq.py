# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:18:14 2022

@author: Alex I
     Create a file "test_max_seq.py" that contains at least three unittest  test cases that test max_seq().  
     Your test class should be called  "TestMaxSequence". 
     Your "tests" should begin with "test_"
     
     abstract a complex step out into a simple function
     The TypeError will occur with a test case that will cause it to be raised.


"""

import unittest
from max_seq import max_seq

class TestMaxSeq(unittest.TestCase):
    def test_empty_list(self):
        """test ValueError raised on empty list"""
        with self.assertRaises(Exception) as context:
            max_seq([])
        self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")

        # with self.assertRaises(Exception) as context:
        #     max_seq(["ignore1","ignore2"])
        # self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")

    def test_incorrect_type(self):
        """test wrong parameter type"""
        with self.assertRaises(Exception) as context:
            max_seq("string argument")
        self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")


    def test_numbers_only(self):
        """test numbers"""
        self.assertEqual(max_seq([ 1, 2, 1, 3, 5, 8, 2, 4, 6, 9]), [1, 2],"logic error")

    def test_mixed_content(self):
        """test mixed content in list"""
        self.assertEqual(max_seq(["test",1,5.0,9]),5.0)

if __name__ == '__main__':
    unittest.main()
