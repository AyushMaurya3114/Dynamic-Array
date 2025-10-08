import ctypes

class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n]=item
        self.n=self.n+1
    
    def pop(self):
        if(self.n==0):
            return 'Empty list'
        print(self.A[self.n-1])
        self.n=self.n-1

    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return 'ValueError- not found'

    def clear(self):
        self.n=0
        self.size=1

    def insert(self,index,item):
        if index < 0 or index > self.n:
            if self.n == self.size:
                self.__resize(self.size*2)
            for i in range(self.n,index,-1):
                self.A[i]=self.A[i-1]
            self.A[index]=item
            self.n=self.n+1

    def __getitem__(self,index):
        if(index > 0 and index<self.n):
            return self.A[index]
        return 'Error- out of bound'
    
    def __delitem__(self,index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds")
        for i in range(index,self.n-1):
            self.A[i]=self.A[i+1]
        self.n=self.n-1

    def remove(self,item):
        pos=self.find(item)

        if(type(pos)==int):
            self.__delitem__(pos)
        else:
            return pos

    def __resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B

    def __str__(self):
        result=''
        for i in range(self.n):
            result=result + str(self.A[i]) + ','
        return '{'+ result[:-1] +'}'
    
    

L=MeraList()

L.append(100)
L.append('hello')
L.append(1400)
L.append(3)
L.append(10230)

print(L[1])
print(L[2])
print(L)

L.pop()
print(L)

print(L.find("hello"))

L.insert(2,"bye")
print(L)

del L[3]
print(L)

L.remove("hello")
print(L)

L.clear()
print(L)

