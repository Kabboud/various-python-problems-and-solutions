import unittest
from hashing import HashTable


class TestHashTable(unittest.TestCase):
    def test_putBeforeResize(self):  # Tests the placing of data in the table prior to resizing
        H = HashTable()  # I chose to insert five values since the initial size of the list is 11 and my
        H[23] = "banana"  # load factor is 0.49
        H[57] = "orange"
        H[35] = "onion"  # This one produces a collision and should move one slot down the list
        H[35] = "artichoke"  # This tests if put is properly replacing at a given location.
        H[41] = "avocado"
        H[66] = "grapefruit"
        expectedResult = [66, 23, 57, 35, None, None, None, None, 41, None, None], \
                         ["grapefruit", "banana", "orange", "artichoke", None, None, None, None, "avocado", None, None]
        generatedResult = H.slots, H.data
        self.assertEqual(expectedResult, generatedResult)

    def test_putAfterResize(self):  # Tests the placing of data in the table after resizing and restructuring
        H = HashTable()
        H[23] = "banana"
        H[57] = "orange"
        H[35] = "onion"  # This one produces a collision and should move one slot down the list
        H[35] = "artichoke"  # This tests if put is properly replacing at a given location.
        H[41] = "avocado"
        H[66] = "grapefruit"
        H[46] = "Guava"  # This should be placed in the list, exceeding the load factor and thus prompting a
        H[97] = "Tomato"  # table resize and restructure of contents.
        H[73] = "Lettuce"
        expectedResult = [23, 46, None, None, 73, 97, None, None, None, None, None, 57, 35, None, None,
                          None, None, None, 41, None, 66, None, None], \
                         ["banana", "Guava", None, None, "Lettuce", "Tomato", None, None, None, None, None, "orange",
                          "artichoke", None, None, None, None, None, "avocado", None, "grapefruit", None, None]
        generatedResult = H.slots, H.data
        self.assertEqual(expectedResult, generatedResult)

    def test_getAfterResize(self):
        H = HashTable()
        H[23] = "banana"
        H[57] = "orange"
        H[35] = "onion"
        H[41] = "avocado"
        H[66] = "grapefruit"
        H[46] = "Guava"  # This should be placed in the list, exceeding the load factor and thus prompting a
        H[97] = "Tomato"  # table resize and restructure of contents.
        H[73] = "Lettuce"
        expectedResult = "banana", "orange", None, "onion", "avocado", None, "grapefruit", "Guava", "Tomato", "Lettuce"
        generatedResult = H[23], H[57], H[32], H[35], H[41], H[45], H[66], H[46], H[97], H[73]
        self.assertEqual(expectedResult, generatedResult)


if __name__ == '__main__':
    unittest.main()
