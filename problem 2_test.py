import unittest
from mySolution import infixToPostfixEval


class TestInfixToPostFixEval(unittest.TestCase):
    def test_equation0(self):
        equation = '4'
        expectedResult = "4 Evaluates to: 4"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)


    def test_equation1(self):
        equation = '( 2 + 2 ) ! + 8'
        expectedResult = "2 2 + ! 8 + Evaluates to: 32"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)

    def test_equation2(self):
        equation = '5*3+2/(2-6)'
        expectedResult = "5 3 * 2 2 6 - / + Evaluates to: 14.5"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)

    def test_equation3(self):
        equation = '((8*3)+9/(3+1)!-9+(2+6))'
        expectedResult = "8 3 * 9 3 1 + ! / + 9 - 2 6 + + Evaluates to: 23.375"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)

    def test_equation4(self):
        equation = '( ( ( ( 2 + 2 ) ! ) ) )'
        expectedResult = "2 2 + ! Evaluates to: 24"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)

    def test_equation5(self):
        equation = '( ( 9 + 9 ) ! + (9 * 9 / 9) - 9) + 9'
        expectedResult = "9 9 + ! 9 9 * 9 / + 9 - 9 + Evaluates to: 6402373705728009.0"
        generatedResult = infixToPostfixEval(equation)
        self.assertEqual(expectedResult, generatedResult)


if __name__ == '__main__':
    unittest.main()
