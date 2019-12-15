"""
Circular Queue이전에 Queue 추상적 자료구조 구현하기. 
큐에 대한 개념도 흔들림.
DoublyLinkedList로 구현하면 dequeue()할 때 연산속도가 상수시간이라 빠르다.
"""

class ArrayQueue:
    def __init__(self):
        self.data = []
        
    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
            
    def enqueue(self, item):
        return self.data.append(item)
    
    def dequeue(self):
        x = self.data.pop(0)
        return x
    
    def peek(self):
        return self.data[0]



