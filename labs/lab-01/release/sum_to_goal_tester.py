# implement here your sum_to_goal tester as instructed.

import unittest
from sum_to_goal import sum_to_goal

class Test(unittest.TestCase):

    def test_middle(self):
        self.assertEqual(sum_to_goal([1, 3, 5, 7, 9], 8), 7)

    def test_first(self):
        self.assertEqual(sum_to_goal([2, 4, 6, 8], 6), 8)

    def test_last(self):
        self.assertEqual(sum_to_goal([1, 2, 10, 20], 30), 200)

    def test_none(self):
        self.assertIsNone(sum_to_goal([1, 2, 3, 4], 100))

    def test_neg(self):
        self.assertEqual(sum_to_goal([-5, -2, 0, 10, 15], 5), -50)

    def test_pair_match(self):
        self.assertEqual(sum_to_goal([4, 6], 10), 24)

    def test_pair_none(self):
        self.assertIsNone(sum_to_goal([4, 6], 5))

if __name__ == "__main__":
    unittest.main()
