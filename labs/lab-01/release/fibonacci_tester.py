# implement here your fibonacci tester as instructed.

import unittest
from fibonacci import fibonacci
 
 
class TestFibonacci(unittest.TestCase):
 
    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)
 
    def test_one(self):
        self.assertEqual(fibonacci(1), 1)
 
    def test_two(self):
        self.assertEqual(fibonacci(2), 1)
 
    def test_five(self):
        self.assertEqual(fibonacci(5), 5)
 
    def test_eight(self):
        self.assertEqual(fibonacci(8), 21)
 
    def test_nine(self):
        self.assertEqual(fibonacci(9), 34)
 
    def test_ten(self):
        self.assertEqual(fibonacci(10), 55)
 
 
if __name__ == "__main__":
    unittest.main()
 
