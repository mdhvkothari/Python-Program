class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appen(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    def show(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


    def appendAtFirst(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def appenAtBetween(self,data,position):
        new_node = Node(data)
        cur_node = self.head
        for i in range(1,position):
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node


    def swap(self,key1,key2):
        prev_1 = None
        cur_node_1 = self.head
        while cur_node_1 and cur_node_1.data!=key1:
            prev_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        prev_2 = None
        cur_node_2 = self.head
        while cur_node_2 and cur_node_2.data!=key2:
            prev_2 = cur_node_2
            cur_node_2 = cur_node_2.next

        if not cur_node_1 or not cur_node_2 :
            return

        if prev_1:
            prev_1.next = cur_node_2
        else:
            self.head = cur_node_2
        
        if prev_2:
            prev_2.next = cur_node_1
        else:
            self.head = cur_node_1

        cur_node_1.next, cur_node_2.next = cur_node_2.next,cur_node_1.next







ll = LinkedList()
ll.appen(1)
ll.appen(2)
ll.appen(3)
ll.appendAtFirst(10)
ll.appenAtBetween(20,2)
ll.swap(10,20)
ll.show()