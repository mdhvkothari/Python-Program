class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data<data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self,data):
        if data<self.data:
            if self.left is None:
                return "Not found"
            return self.left.find(data)
        elif data>self.data:
            if self.right is None:
                return "Not found"
            return self.right.find(data)
        else:
            return "Found!!"

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


node = Node(10)
node.insert(5)
node.insert(50)
node.insert(30)
node.print()
print(node.find(500))

