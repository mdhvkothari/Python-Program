class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

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
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    def print(self):
            cur = self.head
            while cur:
                print(cur.data)
                cur = cur.next

    def delete_node(self,Node):
        cur = self.head
        while cur:
            if cur == Node and cur == self.head:
                #case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    #case 2
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    return
            elif cur == Node:
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
                    cur = None
                    return
            cur = cur.next
    
    def removeDuplicate(self):
        cur = self.head
        dict = {}
        while cur:
            if cur.data not in dict:
                dict[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt   
                #this is because when we delete the node then curent will point to the next node
                
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.removeDuplicate()
dll.print()
