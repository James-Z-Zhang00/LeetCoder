# 21. Merge Two Sorted Lists

# THE FIRST SELF APPROACH

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        result = []

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    result.append(l1.val)
                    l1 = l1.next
                else:
                    result.append(l2.val)
                    l2 = l2.next
            elif l1 and not l2:
                result.append(l1.val)
                l1 = l1.next
            elif not l1 and l2:
                esult.append(l2.val)
                l2 = l2.next
        return result
        
# THE FOUNDED SOLUTION

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
    
# SELF RE-WRITTEN
# 42 ms 16.20 MB
# 68.96% 76.73%


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create an empty ListNode to hold the merged list
        # Where curr will go with the sorted lists and result will always pointing to the beginning of the result ListNode
        curr = result = ListNode()
        # When both of lists have next node
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                # According to test, curr will pointing to the position of list1 before list1 was assigned to list1.next
                # Write in curr = list1; list1 = list1.next would make more sense, same as the case below for list2
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        # When only one of both lists left  
        if list1 or list2:
            curr.next = list1 if list1 else list2
        # Return the starting pointer
        return result.next
    
'''

Firstly create an empty ListNode and make 2 pointers (result and curr) pointing to it.

Then make the curr.next pointing to the ListNode that has smaller value.

Move pointer curr pointing to that ListNode and move the list pointer pointing to the next node.

Repeat the process to re-wire 2 sorted lists.

If they aren't the same length, simply make curr.next pointing to the rest of the longer list.

'''