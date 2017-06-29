import unittest
from PerfectNum import PerfectNum

class PerfectNumTest(unittest.TestCase):
    
    def setUp(self):
        self.pn = PerfectNum()
    
    def tearDown(self):
        self.pn = None
    
    def test_is_perfect1(self):
        pn = PerfectNum()
        self.assertEqual(self.pn.is_perfect(5), False)
    
    def test_is_perfect2(self):
        pn = PerfectNum()
        self.assertEqual(self.pn.is_perfect(6), True)

    def test_is_perfect3git(self):
        pn = PerfectNum()
        self.assertEqual(self.pn.is_perfect(7), False)

if __name__ == '__main__':
    unittest.main()