def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False
    """
    삽입 연산은 아래 if, else문으로 끝난다.
    마지막 if는 처음 노드를 추가할 때 tail을 지정하기 위해서다.
    """
    if pos == 1:
        newNode.next = self.head
        self.head = newNode
    else:
        if pos == self.nodeCount + 1:
            previous = self.tail
        else:
            previous = self.getAt(pos - 1)
        newNode.next = previous.next
        previous.next = newNode
    """
    아래 코드가 처음엔 이해가 안됐는데, 이제 이해가 된다.
    빈리스트에 처음 노드가 추가 된다면 추가한 후에 tail을 추가된 노드로
    지정해야 None으로 남지 않는다. 
    """
    if pos == self.nodeCount + 1:
        self.tail = newNode

    self.nodeCount += 1
    return True
