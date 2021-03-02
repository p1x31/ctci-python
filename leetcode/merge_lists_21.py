# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        "constructor to initiate this object"
        
        # store data
        self.val = x
        
        # store reference (next item)
        self.next = None
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # list to return
        head = ListNode(0)
        ptr = head
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
                
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr = ptr.next
        return head.next


# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(linked_list_str(l2))

# Add linked lists.
s = Solution()
l3 = s.mergeTwoLists(l1, l2)
print(linked_list_str(l3))

print 