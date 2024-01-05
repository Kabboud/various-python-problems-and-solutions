import timeit
import random
import matplotlib.pyplot as plot

# All methods below this line are for median of three quicksort


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partitionMedian(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partitionMedian(alist, first, last):
    pivotIndex = findMedian(alist, first, len(alist)//2, last)
    alist[first], alist[pivotIndex] = alist[pivotIndex], alist[first]
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def findMedian(ls, first, middle, last):
    if ls[first] <= ls[middle] <= ls[last] or ls[last] <= ls[middle] <= ls[first]:
        return middle
    elif ls[first] <= ls[last] <= ls[middle] or ls[middle] <= ls[last] <= ls[first]:
        return last
    return first

# All methods below this line are for regular first index quicksort


def regularQuickSort(alist):
    regularQuickSortHelper(alist, 0, len(alist)-1)


def regularQuickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        regularQuickSortHelper(alist, first, splitpoint - 1)
        regularQuickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


if __name__ == '__main__':
    medianThreeTimes = []
    firstItemTimes = []
    sizeList = list(range(100, 1001, 10))

    for size in sizeList:
        unsorted = [random.randint(0, 500) for i in range(size)]
        tempTimes = []
        for x in range(10):
            start = timeit.default_timer()
            quickSort(unsorted)
            end = timeit.default_timer()
            tempTimes.append(end-start)
        medianThreeTimes.append(float(sum(tempTimes)) / 10)
        tempTimes = []
        for y in range(10):
            start = timeit.default_timer()
            regularQuickSort(unsorted)
            end = timeit.default_timer()
            tempTimes.append(end-start)
        firstItemTimes.append(float(sum(tempTimes)) / 10)

    plot.plot(sizeList, medianThreeTimes, 'ro', label='Median of Three')
    plot.plot(sizeList, firstItemTimes, 'bo', label='First Index')
    plot.legend(loc='upper left')
    plot.ylabel("Time to Sort")
    plot.xlabel("Size of List")
    plot.show()
