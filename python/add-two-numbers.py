class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0 
        for node in [l1, l2]:
            next = True
            value = []
            while node.next:
                value.append(node.val)
                node = node.next
            value.append(node.val)
            value = reversed(value)
            result += int(''.join([str(i) for i in value]))
        result = [int(num) for num in str(result)]
        result_node = None
        first_node = result_node
        for num in reversed(result):
            next_node = ListNode(val=num)
            if result_node:
                result_node.next = next_node
            result_node = next_node
            if not first_node:
                    first_node = result_node
        return first_node