from typing import Optional
from ListNode import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("deleteDuplicates")
        # point to the head initially
        temp = head

        # Loop through all nodes in the linked list
        # Given the linked list is a Singly Linked List
        # Stop the loop until the node.next == None
        while temp and temp.next:

            # Since the linked list is already sorted
            # If the current node.value == node.next.value, then there must be a duplicate and the value only appear adjucent to the current node (as the linked list is sorted)
            # We change the current node.next to node.next.next, i.e. drop the next node
            if temp.val == temp.next.val:
                temp.next = temp.next.next

            # We move to the next node until the current and next node value are distinct
            else:
                temp = temp.next

        return head
