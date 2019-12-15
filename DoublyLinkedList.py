"""
point
-L1.tail의 prev링크와 L2.head의 next링크를 조절한 점. 왜냐하면 두 링크 조절안하면 달랑달랑 붙어있는 상태였다.
-조금 헷갈리긴했지만, L1.tail 을 L2.tail로 바꿔준 것. L2.head 를 L1. head로 바꿔준
"""

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
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

    def getlength(self):
        return self.nodeCount
    
    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev.next.next is None:
            raise IndexError
        else:
            curr = prev.next
            popdata = curr.data
            next = prev.next.next
            
            prev.next = next
            next.prev = prev
            self.nodeCount -= 1
            return popdata


    def popBefore(self, next):
        if next.prev.prev is None:
            raise IndexError
        else:
            curr = next.prev
            prev = next.prev.prev
            popdata = curr.data
            
            prev.next = next
            next.prev = prev
            self.nodeCount -= 1
            return popdata


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            prev = self.getAt(pos-1)
            return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        #L.head = self.head 강사님 함수에는 없는 코드
        
        self.nodeCount += L.nodeCount
        return True
