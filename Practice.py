def factorial(x):
    if x == 2:
        return 2
    else:
        return x * factorial(x-1)


def revList(x):
    if len(x) == 1:
        return x
    else:
        return [x[-1]] + revList(x[:-1])


def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)


