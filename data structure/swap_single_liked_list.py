class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def printList(self):
        curr_list = self.head
        while curr_list:
            print(curr_list.data)
            curr_list = curr_list.next


    def swap(self,key_1,key_2):
        prev_1 = None
        curr_node_1 = self.head
        
        while curr_node_1 and curr_node_1.data!=key_1:
            prev_1 = curr_node_1
            curr_node_1 = curr_node_1.next 

        prev_2 = None
        curr_node_2 = self.head

        while curr_node_2 and curr_node_2.data!=key_2:
            prev_2 = curr_node_2
            curr_node_2 = curr_node_2.next

        if not curr_node_1 or not curr_node_1:
            return

        if prev_1:
            prev_1.next = curr_node_2
        #if we have no previous node which means we are swaping first element with other and first element does not have previous node
        else:
            self.head = curr_node_2

        if prev_2:
            prev_2.next  = curr_node_1
        else:
            self.head = curr_node_1

        #we have to swap current link node
        curr_node_1.next,curr_node_2.next = curr_node_2.next,curr_node_1.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.swap(1,2)
llist.printList()
