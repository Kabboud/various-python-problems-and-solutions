import unittest
from mySolution import power, powerH, C


class TestPower(unittest.TestCase):
    def test_BaseCase(self):
        expectedResult = 1
        generatedResult = power(54, 0, 1)
        self.assertEqual(expectedResult, generatedResult)

    def test_NormalCase(self):
        expectedResult = 27
        generatedResult = power(3, 3, 1)
        self.assertEqual(expectedResult, generatedResult)


class TestPowerH(unittest.TestCase):
    def test_BaseCase1(self):
        expectedResult = 1
        generatedResult = powerH(33, 0)
        self.assertEqual(expectedResult, generatedResult)

    def test_BaseCase2(self):
        expectedResult = 0
        generatedResult = powerH(0, 1)
        self.assertEqual(expectedResult, generatedResult)

    def test_NormalCase(self):
        expectedResult = 32768
        generatedResult = powerH(2, 15)
        self.assertEqual(expectedResult, generatedResult)


class TestC(unittest.TestCase):
    def test_BaseCase(self):
        expectedResult = 1
        generatedResult = C(5, 0)
        self.assertEqual(expectedResult, generatedResult)

    def test_BaseCase2(self):
        expectedResult = 1
        generatedResult = C(5, 5)
        self.assertEqual(expectedResult, generatedResult)

    def test_NormalCase(self):
        expectedResult = 21
        generatedResult = C(7, 2)
        self.assertEqual(expectedResult, generatedResult)


if __name__ == '__main__':
    unittest.main()
