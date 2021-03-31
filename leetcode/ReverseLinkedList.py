# LeetCode 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head:
            current = head
            head = head.next
            current.next = previous
            previous = current
        return previous
            
################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous, current = None, head
        while current:
            current.next, previous, current =  previous, current, current.next
        return previous            

        