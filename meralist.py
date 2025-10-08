import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n += 1
    
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        print(self.A[self.n - 1])
        self.n -= 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError- not found'

    def clear(self):
        self.n = 0
        self.size = 1

    def insert(self, index, item):
    # If index is negative, treat as 0
        if index < 0:
            index = 0
        # If index is greater than current size, append at the end
        if index > self.n:
            index = self.n
        if self.n == self.size:
            self.__resize(self.size * 2)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n += 1

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        return 'Error- out of bound'
    
    def __delitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds")
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        self.n -= 1

    def remove(self, item):
        pos = self.find(item)
        if isinstance(pos, int):
            self.__delitem__(pos)
        else:
            return pos

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __str__(self):
        return '{' + ','.join(str(self.A[i]) for i in range(self.n)) + '}'
