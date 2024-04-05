from attempt_1 import Solution
from TreeNode import TreeNode

def test_attempt_1():
    # test 1
    root_left = TreeNode(9, None, None)

    root_right_right = TreeNode(17, None, None)
    root_right_left = TreeNode(15, None, None)
    root_right = TreeNode(20,root_right_left, root_right_right)

    root = TreeNode(3, root_left, root_right)

    #      3
    #    /   \
    #   9    20
    #        / \
    #      15   17

    assert Solution.maxDepth(self=Solution, root=root) == 3

    # test 2
    node_2 = TreeNode(2, None, None)
    node_1 = TreeNode(1, None, node_2)
    root = node_1

    # 1
    #  \
    #   2

    assert Solution.maxDepth(self=Solution, root=root) == 2
