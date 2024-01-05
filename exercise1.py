import timeit
import random
import matplotlib.pyplot as plot

getTimeList, updateTimeList = [], []
sizeList = list(range(10000, 1000001, 10000))
testUpdateDict = {"A": None, "B": None, "C": None}

for size in sizeList:
    dic = {key: None for key in range(size)}

    neededItem = random.choice(list(dic.keys()))
    start = timeit.default_timer()
    dic.get(neededItem)
    end = timeit.default_timer()
    getTimeList.append(end-start)

    start = timeit.default_timer()
    dic.update(testUpdateDict)
    end = timeit.default_timer()
    updateTimeList.append(end-start)

plot.plot(sizeList, getTimeList, 'ro', label='Get Runtime')
plot.plot(sizeList, updateTimeList, 'bo', label='Update Runtime')
plot.ylim(-0.00001, 0.00001)
plot.legend(loc='upper left')
plot.ylabel("Time to Perform Task")
plot.xlabel("Size of Dictionary")
plot.show()
