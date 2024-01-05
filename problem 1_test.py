import unittest
from mySolution import generate, calcScore


class TestGenerate(unittest.TestCase):
    def test_targetLength(self):
        target = 'tester'
        targetLength = len(target)
        generatedLength = len(generate(target, ''))
        self.assertEqual(targetLength, generatedLength)

    def test_emptyTargetLength(self):
        target = ''
        generatedLength = len(generate(target, ''))
        self.assertEqual(0, generatedLength)

    def test_changeAmount(self):
        target = 'tester'
        changeCounter = 0
        generatedPhrase = generate(target, '')
        secondGenerated = generate(target, generatedPhrase)
        for x in range(len(generatedPhrase)):
            if generatedPhrase[x] != secondGenerated[x]:
                changeCounter += 1
        self.assertEqual(changeCounter, 1)


class TestCalcScore(unittest.TestCase):
    def test_emptyTarget(self):
        target = ''
        generated = generate(target, '')
        score = calcScore(generated, target)
        self.assertEqual(score, 100)

    def test_regularTarget(self):
        target = 'test'
        generated = 'tfga'
        score = calcScore(generated, target)
        self.assertEqual(score, 25)


if __name__ == '__main__':
    unittest.main()
