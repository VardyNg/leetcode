from ListNode import ListNode
from attempt_1 import Solution

def test_attempt_1():
    # test 1
    node1 = ListNode(val=3)
    node2 = ListNode(val=2)
    node3 = ListNode(val=0)
    node4 = ListNode(val=-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    res = Solution.hasCycle(Solution, head=node1)

    assert res is True

    # test 2
    node1 = ListNode(val=1)
    node2 = ListNode(val=2)
    node1.next = node2
    node2.next = node1

    res = Solution.hasCycle(Solution, head=node1)

    assert res is True

    # test 3
    node1 = ListNode(val=1)

    res = Solution.hasCycle(Solution, head=node1)

    assert res is False

    