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
        # Get an empty node to start
        # Keep one pointer always at the starting

        while list1 and list2:
            # When both lists are not empty
            if list1.val < list2.val:
                # Simultaneous assignment
                # For the list and new node (nn) pointer
                list1, nn.next = list1.next, list1
            else:
                # Otherwise assignment for list 2
                list2, nn.next = list2.next, list2
            nn = nn.next
            # Move the new node pointer to the next position
            # For new assignments

        nn.next = list1 if list1 else list2
        # Assign the reset list (could be an empty list)

        return result.next
        # Return the result.next to ignore the initial node
            