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

    assert Solution.minDepth(self=Solution, root=root) == 2
    
    # test 2
    node_6 = TreeNode(6, None, None)
    node_5 = TreeNode(5, None, node_6)
    node_4 = TreeNode(4, None, node_5)
    node_3 = TreeNode(3, None, node_4)
    node_2 = TreeNode(2, None, node_3)
    root = node_2
    
    # 1
    #  \
    #   2
    #    \
    #     3
    #      \
    #       4
    #        \
    #         5
    #          \
    #           6

    assert Solution.minDepth(self=Solution, root=root) == 5
        
    
