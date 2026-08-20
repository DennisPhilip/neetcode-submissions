# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # Find node immediately before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # First node of the section being reversed.
        # It will become the tail.
        tail = prev.next

        # Reverse [left, right]
        curr = prev.next
        prev_node = None

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = nxt

        # Reconnect
        prev.next = prev_node
        tail.next = curr

        return dummy.next