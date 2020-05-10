class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head: ListNode) -> ListNode:
    l = head
    cur = head
    length = 0
    prev = 0
    while cur:
        cur = cur.next
        length+=1
    i=0
    if length == 1:
        return head
    while i <length//2:
        prev = l
        l= l.next
        i+=1
    self.head = None    
    def append(data):
        if self.head == None:
            self.head = ListNode(data)
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = ListNode(data)
    while prev:
        append(prev.val)
        prev = prev.next
    return self.head.next
            