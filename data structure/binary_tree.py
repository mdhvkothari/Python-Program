class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if self.data >data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                     self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
btree = Node(12)
btree.insert(6)
btree.insert(14)
btree.insert(3)
btree.PrintTree()
        