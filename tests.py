import unittest
from wedding import Wedding


class TestWedding(unittest.TestCase):
    def setUp(self):

        self.first_list_from_example = [(1, 2), (2, 4), (3, 5)]
        self.second_list_from_example = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        self.first_wedding = Wedding(self.first_list_from_example,len(self.first_list_from_example))
        self.second_wedding = Wedding(self.second_list_from_example, len(self.second_list_from_example))
        self.first_resault = 4
        self.second_resault = 6

    def test_first_list_from_example(self):
        self.assertEqual(self.first_wedding.number_of_combinations_pairs, self.first_resault)

    def test_second_list_from_example(self):
        self.assertEqual(self.second_wedding.number_of_combinations_pairs, self.second_resault)


if __name__ == '__main__':
    unittest.main()