import unittest
from rerere import start2

class TestSum(unittest.TestCase):

    def test_sum_tuple(self):
        start = [[1,1,1],
                 [0,1,0],
                 [0,1,0]]

        out = [[0,1,0],
                 [1,1,1]]

        number_of_iterations = 1

        result = start2(start,number_of_iterations )
        self.assertEqual(result, out, "Should be 6")

if __name__ == '__main__':
    unittest.main()
