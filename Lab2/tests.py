import unittest
from linked_list import LinkedList
from models import Hamster


class TestHamsters(unittest.TestCase):

    def setUp(self):
        self.hamsters_list = [Hamster(1, 1), Hamster(2, 2), Hamster(3, 4),
                              Hamster(5, 4),Hamster(4, 10), Hamster(12, 11)]
        self.C = len(self.hamsters_list)
        self.hamsters = LinkedList(lambda x: (x.daily_norm + x.greed))



        for item in self.hamsters_list:
            self.hamsters.append(item)

    def test_merge(self):

        index = 0
        self.hamsters.merge_sort(self.hamsters.head)
        for item in range(self.C):
            print( f'sort: {self.hamsters.get_element(item)}')
            print( f'list: {self.hamsters_list[item]}')
            self.assertEqual(self.hamsters.get_element(item), self.hamsters_list[item])





if __name__ == '__main__':
    unittest.main()