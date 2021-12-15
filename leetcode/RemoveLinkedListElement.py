# Leetcode
# 203. Remove Linked List Elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create result_list as dummy list. Assign given list(head) as next
        result_list = ListNode(0)
        result_list.next = head
        # use temp variable as pointer
        temp = result_list
        # Run loop like there is next element. 
        # Since we assigned head as next in result_list, it will iterate thru all the elements
        while temp.next:
            # if next.val has to be removed, skip over to an element after next i.e. next.next
            if temp.next.val == val:
                print(temp.next.next)
                temp.next = temp.next.next
            else:
                temp = temp.next
        # result_list.next is the head of the required LL
        return result_list.next
