from pythonds.basic import Stack
import math


def infixToPostfixEval(equation):
    order = {"!": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    tempList = []  # Tracks the postfix form of the equation
    opStack = Stack()
    numStack = Stack()
    equation = equation.replace(' ', '')  # Removes any whitespace

    for i in range(len(equation)):
        if equation[i] not in order and equation[i] != ")":
            tempList.append(equation[i])
            numStack.push(equation[i])
        elif equation[i] == "(" or opStack.isEmpty():
            opStack.push(equation[i])
        elif equation[i] == ")":
            while opStack.peek() != "(":
                if opStack.peek() != '!':
                    # Used slicing in below line to reverse number order in case two digit characters entered the stack.
                    # This also allowed the performance of evaluations without need of manipulating the stack's order
                    # through an external method.
                    evalStr = opStack.peek().join([numStack.pop()[::-1], numStack.pop()[::-1]])[::-1]
                else:
                    evalStr = 'math.factorial({})'.format(numStack.pop())
                numStack.push(str(eval(evalStr)))
                tempList.append(opStack.pop())
            opStack.pop()  # Gets rid of the '(' in the stack once it has completed its operation
        elif order[equation[i]] > order[opStack.peek()]:
            opStack.push(equation[i])
        else:
            while not opStack.isEmpty() and order[equation[i]] <= order[opStack.peek()]:
                if opStack.peek() != '!':
                    evalStr = opStack.peek().join([numStack.pop()[::-1], numStack.pop()[::-1]])[::-1]
                else:
                    evalStr = 'math.factorial({})'.format(numStack.pop())
                numStack.push(str(eval(evalStr)))
                tempList.append(opStack.pop())
            opStack.push(equation[i])

    while not opStack.isEmpty():  # Completes all final evaluations
        if opStack.peek() != '!':
            evalStr = opStack.peek().join([numStack.pop()[::-1], numStack.pop()[::-1]])[::-1]
        else:
            evalStr = 'math.factorial({})'.format(numStack.pop())
        numStack.push(str(eval(evalStr)))
        tempList.append(opStack.pop())

    total = numStack.pop()
    postfixEquation = ' '.join(tempList)
    return postfixEquation + " Evaluates to: " + total

