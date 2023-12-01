from typing import Optional
from ListNode import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("deleteDuplicates")
        print(head)
        fast = slow = head

        while slow and slow.next:
            
            # if both pointers have the same value
            print(fast.val)
            print(slow.val)
            if fast.val == slow.val:
                print("slow and fast node have the same value")
                # if there is a next node, move the fast pointer to next node
                if fast.next:
                    fast = fast.next
                # otherwise, there is no more node
                # we can savely set slow pointer node's next to None
                else:
                    slow.next = None
            # otherwise, the fast pointer is pointing to a distint node (as compare against the slow pointer )    
            # drop the nodes between slow and fast pointer
            # move slow to the fast pointer
            else:
                print("fast are pointing to a distint value, porinting slow.next = fast")
                slow.next = fast
                slow = fast

        return head
            