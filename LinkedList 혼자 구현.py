class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

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
        
    def traverse(self):
        curr = self.head
        answer = []
        while curr.next:
            answer.append(curr.data)
            curr = curr.next
        return answer
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        else: 
            curr = self.head
            count = 0
            while count < pos:
                count += 1
                curr = curr.next
            return curr
        
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)
            
            if pos == 1:
                if pos == self.nodeCount:
                    popdata = self.head.data
                    self.head = None
                    self.tail = None
                else:
                    popdata = self.head.data 
                    self.head = self.head.next
            else:
                if pos == self.nodeCount:
                    popdata = self.tail.data
                    prev.next = self.tail.next
                    self.tail = prev
                else:
                    popdata = curr.data
                    prev.next = curr.next
        self.nodeCount -= 1
        return popdata

    def popAfter(self, prev):
        if prev.next is None:
            return False
        


    
a = Node(37)
b = Node(17)
c = Node(95)
L = LinkedList()
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)

print(L.getAfter(L.head))
