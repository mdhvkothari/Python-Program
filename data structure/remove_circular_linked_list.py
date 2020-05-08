class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next !=self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self,data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        #if no element in the circular linked list
        if not self.head:
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node



    def remove(self,key):
        if self.head.data==key:
            cur = self.head
            while cur.next!=self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


    def printList(self):
        curr_list = self.head
        while curr_list:
            print(curr_list.data)
            curr_list = curr_list.next
            if curr_list == self.head:
                break



cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.prepend(10)
cll.remove(3)
cll.printList()