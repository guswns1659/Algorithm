"""
재귀적인 방법으로 구현하려면 노드에도 매서드가 필요하다. 
"""
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
        
    def size(self):
        l = self.left.size() if self.left  else 0
        r = self.right.size() if self.right  else 0
        return l + r + 1
        
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        biggerdepth = l if l >= r else r
        return biggerdepth + 1

    def inorder(self):
        traversal = []
        
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = []

        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root :
            return self.root.size()
        else:
            return 0 

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def bft(self):
        traversal = [] 
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
            while not q.isEmpty():
                node = q.dequeue()
                traversal.append(node.data)
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)
            return traversal
        else:
            return traversal

class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]    

a = Node(3)
tree = BinaryTree(a)
print(tree.inorder())
