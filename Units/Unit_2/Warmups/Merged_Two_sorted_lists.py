# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Units.Unit_2.Linked_list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        traverse_list_1, traverse_list_2 = list1, list2
        merged_list = ListNode(0)
        current = merged_list

        while traverse_list_1 and traverse_list_2:
            if traverse_list_1.val <= traverse_list_2.val:
                current.next = traverse_list_1
                traverse_list_1 = traverse_list_1.next
            else:
                current.next = traverse_list_2
                traverse_list_2 = traverse_list_2.next
            current = current.next

        if traverse_list_1:
            current.next = traverse_list_1
        elif traverse_list_2:
            current.next = traverse_list_2

        return merged_list.next

# 1) Instantiate a new node with a value of 0.
#    This will be our dummy node, the node to the left of the head of our return list.
#    Store a reference to this node so that we can return the list at the end.
# 2) Create a pointer, tail, that always points to the end of our LL. Initialize it to point to the dummy node.
# 3) Iterate over the LLs (while head1 or head2) where head1 and head2 are pointers to the heads of the input LLs
#     a) If head1.val <= head2.val, append head1 to the list by pointing tail's next pointer to head1.
#        Move head1 forward one node.
#     b) Otherwise, append head2 to the list by pointing tail's next pointer to head2.
#        Move head2 forward one node
# 4) Move tail forward one node
# 5) Figure out if either list still hasn't been fully traversed.
#    If it hasn't, point tail's next to the head of the list that hasn't been fully traversed.
# 6) Return dummy.next



