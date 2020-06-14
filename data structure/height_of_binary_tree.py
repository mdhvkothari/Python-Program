class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s



class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Btree:
    def __init__(self,root):
        self.root = Node(root)
        

    def preOrder(self,start,traversal):
        if start:
            traversal += (str(start.data)+"-")
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal


    def height(self,node):
        if node is None:
            return -1
        left_node = self.height(node.left)
        right_node = self.height(node.right)
        return 1 + max(left_node,right_node)
    
    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)
            if node.right:
                size+=1
                stack.push(node.right)
        return size

tree = Btree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(4)
tree.root.left.left = Node(5)
print(tree.preOrder(tree.root,""))
print(tree.height(tree.root))
print(tree.size())