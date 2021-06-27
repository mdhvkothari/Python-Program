# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        prev = None
        curr_node = head
        while curr_node:
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next
        head = prev
        return head
        
    def removeNthFromEnd(self, head, n):
        Rhead =  self.reverse(head)
        
        cur_node = Rhead
        prev = 0

        if n == 1:
            Rhead = Rhead.next
            return self.reverse(Rhead)
        else:
            for i in range(1,n):
                prev = cur_node
                cur_node = cur_node.next 
            prev.next = cur_node.next   
            cur_node.next = None
            return self.reverse(Rhead)