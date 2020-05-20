class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur= cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            
    def deletion(self,key):
        cur = self.head
        while cur: 
            if cur.data == key and cur == self.head:
                #case 1
                if cur.next is None:
                    self.head = None
                    cur = None
                    return
                else:
                    #case 2
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                #case3
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    #case4
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur =  None
                    return 
            cur = cur.next







dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.deletion(1)
dll.print()
