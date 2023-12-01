from ListNode import ListNode
from attempt_2 import Solution

def test_attempt_2():
    # test 1
    node1 = ListNode(val=1)
    node2 = ListNode(val=1)
    node3 = ListNode(val=2)
    node1.next = node2
    node2.next = node3

    res = Solution.deleteDuplicates(Solution, node1)

    assert res == node1
    assert res.next == node3
    
    # test 2
    node1 = ListNode(val=1)
    node2 = ListNode(val=1)
    node3 = ListNode(val=2)
    node4 = ListNode(val=3)
    node5 = ListNode(val=3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node5.next = None

    res = Solution.deleteDuplicates(Solution, node1)
    
    assert res == node1
    assert res.next == node3
    assert res.next.next == node4
    assert res.next.next != node5 # even though node4 and node5 have the same value, node5 is removed as it proceeded node4
    
    # test 3
    res = Solution.deleteDuplicates(Solution, None)
    
    assert res == None