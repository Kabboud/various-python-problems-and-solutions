import timeit
import random
import matplotlib.pyplot as plot

listTimes, dictTimes = [], []
sizeList = list(range(10000, 1000001, 10000))

for size in sizeList:
    ls = list(range(size))
    dic = {key: None for key in range(size)}

    deletedItem = random.randrange(size)
    start = timeit.default_timer()
    del ls[deletedItem]
    end = timeit.default_timer()
    listTimes.append(end-start)

    deletedItem = random.choice(list(dic.keys()))
    start = timeit.default_timer()
    del dic[deletedItem]
    end = timeit.default_timer()
    dictTimes.append(end - start)

plot.plot(sizeList, listTimes, 'ro', label="Deleting from List")
plot.plot(sizeList, dictTimes, 'bo', label="Deleting from Dictionary")
plot.legend(loc='upper left')
plot.xlabel("List/Dictionary Size")
plot.ylabel("Time to Perform Task")
plot.show()
