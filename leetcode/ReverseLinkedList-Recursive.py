# LeetCode 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, previous=None) -> ListNode:
        if not head:
            return previous
        current, head.next = head.next, previous
        return self.reverseList(current, head)
    