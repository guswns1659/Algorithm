"""
연결리스트를 끝까지 방문하는 함수를 만들어라.
리턴 값은 방문한 노드의 아이템이 담겨져 있는 리스트다.
예) [34 -> 53 ->32] 인 연결리스트를 순회하고 리턴값을 [34, 53, 32]로 반환

point : curr가 인덱스라는 개념이 확실하지 않았다. 노드의 값은 curr.data인데 계속 curr를 넣음...... 으허..
아쉬운 점은 원래 실습 문제 풀 때, 파이썬으로 실행해보고 문제 푸는데, 이번에는 LinkedList 클래스를 실행하는 법을 몰라서 머리로만 굴려봄.
하지만.. 원인은 단순했다. 

"""

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.countNode = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 and pos > self.countNode:
            return None
        else:
            i = 1
            curr = self.head
            while i < pos:
                i +=1
                curr = curr.next
            return curr

    def traverse(self):
            answer = []
            curr = self.head
            while curr:
                answer.append(curr)
                curr = curr.next
            return answer
            

print(traverse())
