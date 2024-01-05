class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            if self.capacity() > 0.49:  # Resizing the list based on load factor (0.49)
                tempKeys, tempValues = self.slots[:], self.data[:]  # Storing the values of the list before resizing
                self.resize(tempKeys, tempValues)
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                    if self.capacity() > 0.49:
                        tempKeys, tempValues = self.slots[:], self.data[:]
                        self.resize(tempKeys, tempValues)
                else:
                    self.data[nextslot] = data  # replace

    def resize(self, tempKeys, tempValues):
        self.size *= 2  # Doubles the size of the list
        self.findNextPrime(self.size)  # Sets the size of the list to the next prime number
        self.slots, self.data = [None] * self.size, [None] * self.size  # Remaking the lists of keys and values

        for i in range(len(tempKeys)):
            if tempKeys[i] is not None:
                self.put(tempKeys[i], tempValues[i])

    def findNextPrime(self, value):
        while True:
            oldValue = value
            for i in range(2, int(value/2+1)):  # Loops over all possible divisors that could result in remainder 0
                if value % i == 0:
                    value += 1
                    break
            if oldValue == value:
                break
        self.size = value

    def capacity(self):
        occupied = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                occupied += 1
        return float(occupied) / float(self.size)

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
