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





