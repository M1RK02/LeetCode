#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()

        current = result
        while list1 and list2:
            nuovoNodo = ListNode()
            if list1.val <= list2.val:
                nuovoNodo.val = list1.val
                list1 = list1.next
            else:
                nuovoNodo.val = list2.val
                list2 = list2.next

            current.next = nuovoNodo
            current = nuovoNodo

        if not list1:
            current.next = list2
        elif not list2:
            current.next = list1

        return result.next
# @lc code=end
