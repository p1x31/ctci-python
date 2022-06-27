# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        
        middle = self.middleNode(head)
        reverse = self.reverseList(middle)
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True

    

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

    def middleNode(self, head: Optional[ListNode]) -> ListNode:        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow