class Node:
    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode 
            return
        cur = self.root
        while cur.link:
            cur = cur.link
        cur.link = newNode
    def duplicat(self):
        cur = self.root
        prev = None
        d = {}
        while cur:
            if cur.data not in d:
                d[cur.data]  = 1
                prev = cur
            else:
                prev.link = cur.link
            cur = cur.link



    def print(self):
        cur = self.root
        while cur:
            print(cur.data)
            cur= cur.link

ll = LinkedList()
ll.add(20)
ll.add(30)
ll.add(30)
ll.add(40)
ll.print()
ll.duplicat()
ll.print()