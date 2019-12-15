"""
강사님 insertAt() 코드로 안하고 내 껄로 했는데, 오류가 발생한다.
오류는 첫번째 노드를 입력하고 2번째 노드를 입력하려는데, tail이 None이라고 뜸.
강사님 코드랑 비교해보니 if를 많이 썼던 이유가 self.tail에 newnode가 삽입되게 하려고 마지막에 장치를 만들어 놓음.

"""

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
    def __repr__(self):
        if self.nodeCount == 0:
            return "LinkedList: empty"
        s = ""
        curr = self.head
        while curr is not None:
            s +=repr(curr.data)
            if curr.next is not None:
                s+= "->"
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        else:
            i = 1
            curr = self.head
            while i < pos:
                i += 1
                curr = curr.next
            return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        elif pos == self.nodeCount + 1:
            previous = self.tail
            newNode.next = previous.next
            previous.next = newNode
        else:
            previous = self.getAt(pos-1)
            newNode.next = previous.next
            previous.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode
            
        self.nodeCount +=1
        return True

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        i = 1
        result = []
        curr = self.head
        while i <= self.nodeCount:
            i += 1
            result.append(curr.data)
            curr = curr.next
        return result

a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
"""
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
"""
print(L.traverse())



        
