class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def append_at_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,position,data):
        new_node = Node(data)
        cur_node = self.head
        for i in range(1,position):
            cur_node = cur_node.next
        
        new_node.next = cur_node.next
        cur_node.next = new_node


    def delete(self,key):
        cur_node = self.head
        if cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

    def length_list(self):
        len =0
        curr_node = self.head
        while curr_node:
            len += 1
            curr_node = curr_node.next
        return len          
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
# llist.append_at_first(5)
llist.insert_after_node(2,20)
# llist.print_list()
llist.delete(1)
llist.print_list()
llist.length_list()
