"""
배열리스트로 스택의 추상적 자료구조 구현하기
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
    
from pythonds.basic.stack import Stack
S = Stack()
print(dir(S))
