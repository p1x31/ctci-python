# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head):
    #return the middle node of the linked list.
    #If there are two middle nodes, return the second middle node.
    #if there are odd number of nodes, return the middle node.
    #if there are even number of nodes, return the second middle node.
    #if there are no nodes, return None.
    #if there is only one node, return the node.
    # While slow moves one step forward, fast moves two steps forward.
    # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
print(middleNode([1,2,3,4,5]))
print(middleNode([1,2,3,4,5,6]))