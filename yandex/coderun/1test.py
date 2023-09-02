import unittest
from first import solve
class TestSolve(unittest.TestCase):
    def test_case1(self):
        N = 5
        A = [1, 3, 5, 7, 9]
        self.assertEqual(solve(N, A), 6)

    def test_case2(self):
        N = 4
        A = [2, 4, 6, 8]
        self.assertEqual(solve(N, A), 4)

    def test_case3(self):
        N = 3
        A = [1, 5, 9]
        self.assertEqual(solve(N, A), 8)

    def test_case4(self):
        N = 2
        A = [3, 7]
        self.assertEqual(solve(N, A), 4)


if __name__ == '__main__':
    unittest.main()