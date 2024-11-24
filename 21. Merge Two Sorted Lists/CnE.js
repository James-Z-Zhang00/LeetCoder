/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = (list1, list2) => {

    var initialNode = curr = {var:0, next: null}
    // Get an empty node to start

    while (list1 && list2) {
        // When both lists are not empty
        list1.val < list2.val ? [curr.next, list1] = [list1, list1.next] : [curr.next, list2] = [list2, list2.next]
        // Simutaneous assignment according to value (val)
        curr = curr.next
        // Move the new node pointer to the next position
        // For new assignments
    }
    curr.next = list1 || list2
    // Assign the reset list (could be an empty list)
    return initialNode.next
    // Return the result.next to ignore the initial node
};