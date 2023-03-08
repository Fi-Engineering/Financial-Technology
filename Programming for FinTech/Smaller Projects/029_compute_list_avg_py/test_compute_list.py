import unittest
from compute_list_avg import compute_average

class TestComputeAverage(unittest.TestCase):
    def test_empty_list(self):
        """test ValueError raised on empty list"""
        with self.assertRaises(Exception) as context:
            compute_average([])
        self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")

        with self.assertRaises(Exception) as context:
            compute_average(["ignore1","ignore2"])
        self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")

    def test_incorrect_type(self):
        """test wrong parameter type"""
        with self.assertRaises(Exception) as context:
            compute_average("string argument")
        self.assertTrue(type(context.exception) == ValueError,"Wrong exception type raised")


    def test_numbers_only(self):
        """test numbers"""
        self.assertEqual(compute_average([1,5,9,13,17]),9.0,"Incorrect result")

    def test_mixed_content(self):
        """test mixed content in list"""
        self.assertEqual(compute_average(["test",1,5.0,9]),5.0)
