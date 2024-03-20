from attempt_1 import Solution
from TreeNode import TreeNode

def test_attempt_1():
    # test 1
    root_left_left = TreeNode(3, None, None)
    root_left_right = TreeNode(4, None, None)
    root_left = TreeNode(2, root_left_left, root_left_right)

    root_right_right = TreeNode(3, None, None)
    root_right_left = TreeNode(4, None, None)
    root_right = TreeNode(2,root_right_left, root_right_right)

    root = TreeNode(1, root_left, root_right)
    
    #      1
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
   
    assert Solution.isSymmetric(self=Solution, root=root) is True
    
    # test 2
    root_left_left = None
    root_left_right = TreeNode(4, None, None)
    root_left = TreeNode(2, root_left_left, root_left_right)

    root_right_right = TreeNode(3, None, None)
    root_right_left = None
    root_right = TreeNode(2,root_right_left, root_right_right)

    root = TreeNode(1, root_left, root_right)
    
    #      1
    #    /   \
    #   2     2
    #    \     \
    #     3     3
    
    assert Solution.isSymmetric(self=Solution, root=root) is False