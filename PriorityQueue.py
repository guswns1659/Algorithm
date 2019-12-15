from DoublyLinkedList import Node, DoublyLinkedList
    
"""
우선순위는 크기가 작으면 뒤로 삽입
"""
class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0:

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next.next and newNode.data < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)
        return True

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self)
        return self.queue.getAt(self.queue.getLength()).data


        
        
        
