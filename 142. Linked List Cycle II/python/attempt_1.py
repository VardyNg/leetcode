from typing import Optional
from ListNode import ListNode

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("detectCycle")
        hashset = set()

        temp = head
        if temp:
            hashset.add(temp)

        while temp and temp.next:
            print(temp.val)
            if temp.next in hashset:
                return temp.next

            hashset.add(temp.next)
            temp = temp.next

        return None
