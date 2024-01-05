import unittest
from eval import evalTree


class TestEvalTree(unittest.TestCase):
    def test_bigTree(self):
        tree = ["*", ["+", ["a", [], []], ["b", [], []]], ["/", ["c", [], []], ["d", [], []]]]
        env = [["a", 10], ["b", 20], ["c", 30], ["d", 15]]
        expectedResult = 60
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_prenumTree(self):
        tree = ["10", [], []]
        env = [["a", 10], ["b", 20], ["c", 30]]

    def test_OneValueTree(self):
        tree = ["x1", [], []]
        env = [["a", 10], ["x1", 22]]
        expectedResult = 22
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_DivisionZeroTree(self):
        tree = ["/", ["a", [], []], ["0", [], []]]
        env = [["a", 10], ["x1", 22]]
        expectedResult = None
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_regularTree(self):
        tree = ["*", ["b", [], []], ["c", [], []]]
        env = [["a", 10], ["b", 20], ["c", 30]]
        expectedResult = 600
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_bigTree2(self):
        tree = ["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]]
        env = [["a", 10], ["b", 20], ["c", 30]]
        expectedResult = 610
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_mirroredTree(self):
        tree = ["+", ["*", ["b", [], []], ["c", [], []]], ["a", [], []]]
        env = [["a", 10], ["b", 20], ["c", 30]]
        expectedResult = 610
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_mirroredTree2(self):
        tree = ["*", ["/", ["c", [], []], ["d", [], []]], ["+", ["a", [], []], ["b", [], []]]]
        env = [["a", 10], ["b", 20], ["c", 30], ["d", 15]]
        expectedResult = 60
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_missingValueTree(self):
        tree = ["+", ["a", [], []], ["*", ["b", [], []], ["c", [], []]]]
        env = [["b", 20], ["c", 30]]
        expectedResult = None
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_allMissingValueTree(self):
        tree = ["*", ["+", ["e", [], []], ["f", [], []]], ["/", ["g", [], []], ["h", [], []]]]
        env = [["b", 20], ["c", 30]]
        expectedResult = None
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)

    def test_emptyEnvironmentTree(self):
        tree = ["*", ["+", ["a", [], []], ["b", [], []]], ["/", ["c", [], []], ["d", [], []]]]
        env = []
        expectedResult = None
        generatedResult = evalTree(tree, env)
        self.assertEqual(expectedResult, generatedResult)


if __name__ == '__main__':
    unittest.main()
