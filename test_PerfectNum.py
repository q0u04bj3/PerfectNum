import unittest
from PerfectNum import is_perfect

class PerfectNumTest(unittest.TestCase):
    
    def test_is_perfect1(self):
        self.assertEqual(is_perfect(5), False)
    
    def test_is_perfect2(self):
        self.assertEqual(is_perfect(6), True)

    def test_is_perfect3(self):
        self.assertEqual(is_perfect(7), False)

        
if __name__ == '__main__':
    unittest.main()
