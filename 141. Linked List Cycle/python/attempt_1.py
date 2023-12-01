from typing import Optional
from ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # if there is a cycle in the list, it means there is a node being pointed twice
        # use a set to record all reference of node's next
        # if a node's next is already present in the set
        # it means there is a cycle
        hashset = set()

        temp = head
        has_cycle = False
        while temp and temp.next and not has_cycle:
            if temp.next in hashset:
                has_cycle = True
            else:
                hashset.add(temp.next)

            temp = temp.next

        return has_cycle
