class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)        
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
        
    def traverse(self): #DoubleLinkedList
        curr = self.head
        answer = []
        while curr.next.next: 
            curr = curr.next
            answer.append(curr.data)
        return answer
    
    def getAt(self, pos): #DoubleLinkedList
        if pos < 0 or pos > self.nodeCount:
            return None
        else: 
            curr = self.head
            count = 0
            while count < pos:
                count += 1
                curr = curr.next
            return curr
        
    def insertAt(self, pos, newNode): #DoubleLinkedList
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)

    def insertAfter(self, prev, newNode): #DoubleLinkedList
        later = prev.next
        newNode.next = later
        newNode.prev = prev
        later.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            prev = self.getAt(pos-1)
        return self.popAfter(prev)

    def popAfter(self, prev):
        if prev.next.next is None:
            return False
        else:
            curr = prev.next
            popdata = curr.data
            prev.next = curr.next
            curr.next.prev = prev
            self.nodeCount -= 1
            return popdata

    def popBefore(self, later):
        if later.prev.prev is None:
            return False
        else:
            curr = later.prev
            prev = later.prev.prev
            popdata = curr.data

            later.prev = prev
            prev.next = later
            self.nodeCount -= 1
            return popdata

a = Node(37)
b = Node(17)
c = Node(95)
L = DoubleLinkedList()
L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)

print(L.popBefore(c))
print(L)
