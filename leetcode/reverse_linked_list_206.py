# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        prev = None
        curr = head
        while curr:
            # save next node
            next = curr.next
            # reverse next node
            curr.next = prev
            # move prev and curr
            prev = curr
            # move curr to next
            curr = next
        return prev