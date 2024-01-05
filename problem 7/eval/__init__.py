def evalTree(tree, environment, env=False):
    if tree is None:
        return None
    else:
        newTree = tree[:]
        if env is False:
            newTree = fillTree(tree, environment)
        if len(newTree[1])+len(newTree[2]) == 0:
            return newTree[0]
        else:
            evalStr = str(evalTree(newTree[1], [], True)) + str(newTree[0]) + str(evalTree(newTree[2], [], True))
    return int(eval(evalStr)) if str(invalidCheck(evalStr))[-2:] == '.0' else invalidCheck(evalStr)


def invalidCheck(evalStr):
    try:
        num = eval(evalStr)
        return num
    except ValueError:
        return False
    except ZeroDivisionError:
        return None
    except NameError:
        return None
    except TypeError:
        return None


def fillTree(tree, environment):
    newTree = tree[:]
    if len(newTree[1])+len(newTree[2]) == 0:
        for item in environment:
            if item[0] == newTree[0]:
                newTree[0] = item[1]
        if type(newTree[0]) == str and invalidCheck(newTree[0]) is True:
            newTree[0] = invalidCheck(newTree[0])
        return newTree
    else:
        newTree[1] = fillTree(newTree[1], environment)
        newTree[2] = fillTree(newTree[2], environment)
        return newTree
