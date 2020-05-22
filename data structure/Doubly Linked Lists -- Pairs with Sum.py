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

    def pair_with_sum(self,sum_val):
        sums = []
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if q.data + p.data == sum_val:
                    sums.append("("+str(p.data)+","+str(q.data)+")")
                q = q.next
            p = p.next
        return sums

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll.pair_with_sum(5))
dll.print()