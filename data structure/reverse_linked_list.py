class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def printList(self):
        curr_list = self.head
        while curr_list:
            print(curr_list.data)
            curr_list = curr_list.next

    def reverse(self):
        prev = None
        curr_node = self.head
        while curr_node:
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next
        self.head = prev



llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.reverse()
llist.printList()