# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traversed = []
        while head and head.next:
            next_node = head.next
            head.next = None
            traversed.append(head)
            head = next_node
        new_head = head
        while traversed:
            new_head.next = traversed.pop()
            new_head = new_head.next
        return head
