"""
key point : 강의 속 강사님 코드가 이해 안되서 내가 코드를 작성하고 돌려보니 안되더라..
손으로 그렸을 땐 출력이 올바른데, 값이 이상했다. 강사님꺼로 하자해서 복사해오니 뭔가 기분이 쎄한 것..
코드 비교해보니 프린트 기능하는 함수가 잘 못 입력되어 있었다. !!
중요한 점은 포기하지 않고 내 생각대로 코드를 작성해본 것!! 


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
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L.insertAt(1,a))
print(L)
print(L.insertAt(2,b))
print(L)
print(L.insertAt(1,c))
print(L)
