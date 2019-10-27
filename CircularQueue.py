#환형큐 구현


class CircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.rear = -1
        self.front = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x): 
        if self.isFull():
            raise IndexError('Queue is full')
        else:
            self.rear = (self.maxCount + self.rear + 1) % self.maxCount
            self.data[self.rear] = x
            self.count += 1
            
    def dequeue(self): #반환은 L[index]로 하면된다. 어차피 덮어쓴다.
        if self.isEmpty():
            raise IndexError('Queue is Empty')
        else:
            self.front = (self.maxCount + self.front + 1) % self.maxCount
            x = self.data[self.front] 
            self.count -= 1
            return x
        
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue is Empty')
        return self.data[(self.maxCount + self.front + 1) % self.maxCount]
