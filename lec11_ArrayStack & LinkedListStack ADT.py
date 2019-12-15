"""
배열리스트와 연결리스트로 스택의 추상적 자료구조 구현하기
연산의 정의
-길이 얻어내기 : size()
-비었는지 확인하기 : isEmpty()
-push 하기 : push()
-pop 하기 : push()
-peek 하기 : peek()
"""

class ArrayStack:
    def __init__(self):
        self.data = []
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        return self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    
#폴더 내 모듈 중 import 하려면 폴더에 __init__파일 필요.
from DoubleLinkedList_ADT import Node
from DoubleLinkedList_ADT import DoublyLinkedList

class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    def size(self):
        return self.data.getLength()
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size()+1, node) #self.size()에 삽입은 마지막 전에 삽입
    def pop(self):
        return self.data.popAt(self.size())
    def peek(self):
        return self.data.getAt(self.size()).data
