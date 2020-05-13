class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)


        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next!=self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
    def printList(self):
        curr_list = self.head
        while curr_list:
            print(curr_list.data)
            curr_list = curr_list.next
            if curr_list == self.head:
                break
    #for override function we use __functionName__
    def __len__(self):
        cur = self.head
        count=0
        while cur:
            count+=1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size//2
        count=0
        prev = None
        cur = self.head
        while cur and count <mid:
            count +=1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        #last node data
        split_cllist.append(cur.data)
        self.printList()
        print('\n')
        split_cllist.printList()

cl = CircularLinkedList()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.printList()
print('\n')
cl.split_list()