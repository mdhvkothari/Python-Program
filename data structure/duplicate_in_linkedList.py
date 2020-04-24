class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head =  None

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



    def removeDuplicate(self):
        prev = None
        cur_node =self.head

        dup_value = {}

        while cur_node:
            if cur_node.data in dup_value:
                #if we find duplicate node 
                prev.next = cur_node.next
            else:
                dup_value[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next

ll = linkedList()
ll.append(1)
ll.append(5)
ll.append(5)
ll.append(2)
ll.removeDuplicate()
ll.printList()