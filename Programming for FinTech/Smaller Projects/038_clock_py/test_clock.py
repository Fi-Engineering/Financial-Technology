from clock import MyClock24
import unittest

class TestClock(unittest.TestCase):
        
    def test_create(self):
        """ test creation """
 
        a = MyClock24(1,5,30)
        self.assertEqual(str(a),"01:05:30")

        b = MyClock24(25,5,30)
        self.assertEqual(str(b),"01:05:30")

    def test_str(self):
        """ test __str__ works correctly - formatting """
        a = MyClock24(7,7,7)
        self.assertEqual(str(a),"07:07:07")

        b = MyClock24(23,59,59)
        self.assertEqual(str(b),"23:59:59")

    def test_repr(self):
        """ testing __repr__ """
        import ast

        b = MyClock24(23,59,58)
        self.assertEqual(ast.literal_eval(repr(b)),{'hours': 23, 'minutes': 59, 'seconds': 58})

    def test_properties(self):
        """ test access comparisons """
        a = MyClock24(23,59,58)
        self.assertEqual(a.hours,23)
        self.assertEqual(a.minutes,59)
        self.assertEqual(a.seconds,58)

    def test_comparisons(self):
        """ test that the magic methods implemented for comparisons """
        a = MyClock24(23,59,58)
        b = MyClock24(47,59,58)
        c = MyClock24(0,0,0)

        self.assertTrue(a == b)
        self.assertFalse(a == c)

        self.assertFalse(a != b)
        self.assertTrue(a != c)

        self.assertTrue(a  >  c)
        self.assertTrue(a >= b)

        self.assertTrue(c < a )
        self.assertTrue(b <= a)

    def test_arithmetic(self):
        """ test arithmetic """
        a = MyClock24(23,59,58)
        b = a + 3
        self.assertEqual(str(b),"00:00:01")
        c = b - 3
        self.assertTrue( a == c)

        b = MyClock24(0,0,3)
        c = a + b
        self.assertEqual(str(c),"00:00:01")
        d = c - b
        self.assertTrue( a == d)

    def test_tick(self):
        """ test tick()"""
        a = MyClock24(23,59,0)
        for i in range(70):
            a.tick()
        self.assertEqual(str(a),"00:00:10")
