from attempt_1 import Solution
from TreeNode import TreeNode

def test_attempt_1():
    # test 1
    p_left = TreeNode(2, None, None)
    p_right = TreeNode(3, None, None)
    p = TreeNode(1,p_left, p_right)

    q_left = TreeNode(2, None, None)
    q_right = TreeNode(3, None, None)
    q = TreeNode(1,q_left, q_right)

    # p Tree      q Tree
    #    1          1
    #   / \        / \
    #  2   3      2   3


    is_same_tree = Solution.isSameTree(self=Solution, p=p, q=q)

    assert is_same_tree is True

    # test 2

    p_left = TreeNode(2, None, None)
    p_right = TreeNode(1, None, None)
    p = TreeNode(1,p_left, p_right)

    q_left = TreeNode(1, None, None)
    q_right = TreeNode(2, None, None)
    q = TreeNode(1, None, q_right)

    # p Tree      q Tree
    #    1          1
    #   / \        / \
    #  2   1      1   2

    is_same_tree = Solution.isSameTree(self=Solution, p=p, q=q)
    assert is_same_tree is False

    # test 3

    p_left = TreeNode(2, None, None)
    p = TreeNode(1,p_left, None)

    q_right = TreeNode(2, None, None)
    q = TreeNode(1, None, q_right)

    # p Tree      q Tree
    #    1          1
    #   /            \
    #  2              2

    is_same_tree = Solution.isSameTree(self=Solution, p=p, q=q)
    assert is_same_tree is False
