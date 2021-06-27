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
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        
        cur_node.next = new_node

    def printList(self):
        curr_list = self.head
        while curr_list:
            print(curr_list.data)
            curr_list = curr_list.next

    # 1->2->3->3->4
    def remove(self,index):
        cur_node = self.head
        prev = 0

        if index == 1:
            self.head = self.head.next
        else:
            for i in range(1,index):
                prev = cur_node
                cur_node = cur_node.next 
            # if cur_node.next==None:
                
            print(prev.data)
            print(cur_node.data)
            prev.next = cur_node.next
            cur_node.next = None

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.printList()
ll.remove(1)
ll.printList()
