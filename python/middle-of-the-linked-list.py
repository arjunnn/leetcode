# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # nodes = 1
        # current = head
        # while current.next:
        #     current = current.next
        #     nodes += 1
        # if nodes % 2 == 0:
        #     nodes = (nodes / 2) + 1
        # else:
        #     nodes = ceil(nodes/2)
        # current = head
        # while nodes > 1:
        #     current = current.next
        #     nodes -= 1
        # return current

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
