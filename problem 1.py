import random
import matplotlib.pyplot as plot


def monkeyTypist():
    target = list(input("What String should the monkey attempt to type? (Do not use any special characters)").lower())
    epoch = 0
    totalEpoch = 0
    bestStr = generate(target, '')
    bestScore = calcScore(bestStr, target)
    epochValues = [0]
    scoreValues = [bestScore]
    while bestScore < 100:
        newStr = generate(target, bestStr)
        newScore = calcScore(newStr, target)
        if newScore > bestScore:
            bestStr = newStr
            bestScore = newScore
            epochValues.append(totalEpoch)
            scoreValues.append(bestScore)
        if epoch == 100 and bestScore != 100:
            print("{0} {1:.6f} {2}".format(bestStr, bestScore, totalEpoch))
            epoch = 0
        epoch += 1
        totalEpoch += 1
        if bestScore == 100:
            epochValues.append(totalEpoch)
            scoreValues.append(bestScore)

    print("{0} {1:.6f} {2}".format(bestStr, bestScore, totalEpoch))
    plot.plot(epochValues, scoreValues, 'ro')
    plot.ylabel("Scores of Best String")
    plot.xlabel("Number of Iterations")
    plot.show()


def generate(target, phrase):
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    for x in range(len(target)):
        if len(phrase) >= len(target):
            phrase = list(phrase)
            if phrase[x] != target[x]:
                phrase[x] = random.choice(alphabet)
                break
        else:
            phrase += random.choice(alphabet)

    return "".join(phrase)


def calcScore(phrase, target):

    correct = 0.0

    for x in range(len(target)):
        if phrase[x] == target[x]:
            correct += 1.0

    if len(phrase) != 0:
        return correct/len(target)*100
    else:
        return 100
