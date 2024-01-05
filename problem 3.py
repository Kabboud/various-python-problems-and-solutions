import turtle
import random


def tree(branchLength, t):
    # Random factors by which the function decides to turn the turtle for the purpose of randomizing
    # the look of the tree.
    rightTurn = random.randrange(25, 45)
    leftTurn = random.randrange(25, 45)
    # Random factor deciding by what length the branches should be cut with each recursive call.
    leftCut = random.randrange(10, 12)
    rightCut = random.randrange(10, 12)

    if branchLength > 5:
        # Changing the color of the branch so that as it gets smaller, it begins to look like leaves.
        if branchLength > 20:
            t.color("brown")
        else:
            t.color("green")

        #  As the branch length gets smaller, the branches will also become less wide.
        thickness = branchLength / 8
        t.width(thickness)

        t.forward(branchLength)
        t.right(rightTurn)
        tree(branchLength-rightCut, t)
        t.left(leftTurn + rightTurn)
        tree(branchLength-leftCut, t)
        t.right(leftTurn)
        t.backward(branchLength)


def main():
    t = turtle.Turtle()
    t.speed(0)
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    window.exitonclick()


def power(x, n, acc=1):
    if n == 0:
        return acc
    else:
        return power(x, n-1, acc*x)


def powerH(x, n):
    if n == 0:
        return 1
    elif n == 1 or x == 0:
        return x
    else:
        return (x**(int(n/2)))**2 * powerH(x, n - (2 * int(n/2)))


def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return int(float(n) / float(k) * C(n-1, k-1))
