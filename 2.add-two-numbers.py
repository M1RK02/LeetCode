#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        somma = 0
        
        current = result
        while(l1 or l2 or somma != 0):
            
            if(l1):
                somma += l1.val
                l1 = l1.next
            
            if(l2):
                somma += l2.val
                l2 = l2.next
            
            nuovoNodo = ListNode()
            nuovoNodo.val = somma%10
            current.next = nuovoNodo
            current = nuovoNodo
            
            somma = int(somma/10);

        return result.next
# @lc code=end