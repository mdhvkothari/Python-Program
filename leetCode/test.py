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
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def rotate(self,first,second):
        onePrev = None
        one = self.head
        twoNext = None
        two = self.head
        for i in range(1,first):
            onePrev = one
            one = one.next
        print(one.data,onePrev.data)
        for j in range(1,second):
            two = two.next
        twoNext = two.next
        print(two.data,twoNext.data)
        two.next = onePrev
        one.next = twoNext
        


    
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.rotate(2,4)
llist.print_list()