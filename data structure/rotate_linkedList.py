class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head == None:
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

    def rotate(self,index):
        p = self.head
        q = self.head
        perv = None

        for i in range(1,index):
            perv = p
            p = p.next
            q = q.next
        p = perv
        #we have to point q to the last node in the list
        while q:
            perv = q
            q = q.next
        q = perv

        q.next = self.head
        self.head = p.next
        p.next = None        

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.rotate(3)
ll.printList()

