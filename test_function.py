import unittest
from qwer import ini

class TestSum(unittest.TestCase):

    def test_glider(self):

        out = '▓▓░░▓▓\n░░▓▓▓▓\n░░▓▓░░\n'

        seed = open('./glider.txt').read()

        number_of_iterations = 101

        result = ini(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

if __name__ == '__main__':
    unittest.main()
