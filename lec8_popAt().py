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
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)

            if pos == 1:
                if self.nodeCount == 1:
                    popdata = self.head.data
                    self.head = None
                    self.tail = None
                else:
                    popdata = self.head.data
                    self.head = self.head.next
            else:
                if pos == self.nodeCount :
                    popdata = self.tail.data
                    prev.next = self.tail.next
                    self.tail = prev
                else:
                    popdata = curr.data
                    prev.next = curr.next
                    
        self.nodeCount -= 1
        return popdata
            
    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
    
    def getAfter(self, prev):
        return prev.next



a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)
L.getAfter(b)

