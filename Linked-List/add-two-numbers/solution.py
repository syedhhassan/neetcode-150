# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        carry = 0
        newHead = ListNode()
        curr = newHead
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            summ = val1 + val2 + carry

            carry = summ // 10
            curr.next = ListNode(summ % 10)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        
        return newHead.next