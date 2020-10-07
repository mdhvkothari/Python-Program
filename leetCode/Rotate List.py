class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def adding(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        curNode.next = newNode

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    def rotate(self,number):
        for i in range(0,number):
            head_node = self.head
            cur_node = self.head
            prev =None
            while cur_node.next:
                prev = cur_node
                cur_node = cur_node.next
            
            cur_node.next = self.head
            self.head = cur_node
            prev.next = None



ll = LinkedList()
ll.adding(10)
ll.adding(20)
ll.adding(30)
ll.adding(40)
ll.rotate(2)
ll.print()