'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nn = result = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                nn.next = list1
                list1, nn = list1.next, list1
            else:
                nn.next = list2
                list2, nn = list2.next, list2
        if list1 or list2:
            nn.next = list1 if list1 else list2

        result = result.next
        
        return result
            