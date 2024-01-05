import unittest
from sorting import partitionMedian, findMedian


class testFindMedian(unittest.TestCase):
    def test_smallList(self):
        ls = [1, 2, 3]
        medianIndex = findMedian(ls, 0, len(ls) // 2, len(ls) - 1)
        result = len(ls) // 2
        self.assertEqual(medianIndex, result)

    def test_largeList(self):
        ls = [10, 2, 3, 7, 9, 4, 6, 9, 2, 4, 11, 15, 13, 17, 13, 22, 20]
        medianIndex = findMedian(ls, 0, len(ls) // 2, len(ls) - 1)
        result = 0
        self.assertEqual(medianIndex, result)

    def test_evenList(self):
        ls = [25, 10, 2, 3, 7, 9, 4, 6, 9, 2, 4, 11, 15, 13, 17, 13, 22, 20]
        medianIndex = findMedian(ls, 0, len(ls) // 2, len(ls) - 1)
        result = len(ls) - 1
        self.assertEqual(medianIndex, result)


class testPartition(unittest.TestCase):
    def test_medianPartition(self):
        ls = [25, 10, 2, 3, 7, 9, 4]
        switchIndex = partitionMedian(ls, 0, len(ls) - 1)
        expectedIndex = 2
        self.assertEqual(switchIndex, expectedIndex)

    def test_medianPartition2(self):
        ls = [2, 3, 4, 10, 7, 9, 25]
        switchIndex = partitionMedian(ls, 0, len(ls) - 1)
        expectedIndex = 5
        self.assertEqual(switchIndex, expectedIndex)

    def test_medianPartitionEven(self):
        ls = [9, 4, 6, 7, 2, 3]
        switchIndex = partitionMedian(ls, 0, len(ls) - 1)
        expectedIndex = 4
        self.assertEqual(switchIndex, expectedIndex)


if __name__ == '__main__':
    unittest.main()
