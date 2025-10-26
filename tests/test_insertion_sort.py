import unittest
from insertion_sort import insertion_sort_desc

class TestInsertionSortDesc(unittest.TestCase):
    def test_basic(self):
        data = [8, 3, 1, 7, 0, 10, 2]
        self.assertEqual(insertion_sort_desc(data[:]), [10, 8, 7, 3, 2, 1, 0])

    def test_already_desc(self):
        self.assertEqual(insertion_sort_desc([9, 7, 5]), [9, 7, 5])

    def test_all_equal(self):
        self.assertEqual(insertion_sort_desc([4,4,4]), [4,4,4])

    def test_negatives(self):
        self.assertEqual(insertion_sort_desc([0, -1, -3, 2]), [2, 0, -1, -3])

    def test_empty_list(self):
        self.assertEqual(insertion_sort_desc([]), [])

if __name__ == "__main__":
    unittest.main()
