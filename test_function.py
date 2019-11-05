import unittest
from fini import game

class TestSum(unittest.TestCase):

    def test_glider(self):

        out = ('▓▓░░▓▓\n'
               '░░▓▓▓▓\n'
               '░░▓▓░░\n')

        f = open('./glider.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

    def test_empty(self):

        out = 'No living cells in initial seed\n'

        f = open('./empty.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

    def test_block(self):

        out = ('░░░░▓▓▓▓░░░░\n'
               '░░▓▓░░░░▓▓░░\n'
               '▓▓░░░░░░░░▓▓\n'
               '▓▓░░░░░░░░▓▓\n'
               '░░▓▓░░░░▓▓░░\n'
               '░░░░▓▓▓▓░░░░\n')

        f = open('./block.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

if __name__ == '__main__':
    unittest.main()
