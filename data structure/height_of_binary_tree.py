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


tree = Btree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(4)
tree.root.left.left = Node(5)
print(tree.preOrder(tree.root,""))
print(tree.height(tree.root))