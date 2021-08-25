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

    def remove(self,a):
        cur = self.head 
        prev = None

        while True:
            if cur == None:
                break
            if cur.data == a:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                    prev = None
            else:
                prev = cur
            cur = cur.next
                






llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(4)
llist.printList()
llist.remove(4)
llist.printList()