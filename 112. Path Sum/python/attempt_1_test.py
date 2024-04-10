from attempt_1 import Solution
from TreeNode import TreeNode

def test_attempt_1():

    # test 1
    lv4_1_node = TreeNode(val=7)
    lv4_2_node = TreeNode(val=2)
    lv4_3_node = TreeNode(val=1)

    lv3_1_node = TreeNode(val=11, left=lv4_1_node, right=lv4_2_node)
    lv3_2_node = TreeNode(val=13)
    lv3_3_node = TreeNode(val=4, right=lv4_3_node)

    lv2_1_node = TreeNode(val=4, left=lv3_1_node)
    lv2_2_node = TreeNode(val=8, left=lv3_2_node, right=lv3_3_node)

    root_node = TreeNode(val=5, left=lv2_1_node, right=lv2_2_node)

    assert Solution.hasPathSum(self=Solution, root=root_node, targetSum=22) is True

    # test 2
    lv2_1_node = TreeNode(val=2)
    lv2_2_node = TreeNode(val=3)
    root_node = TreeNode(val=1, left=lv2_1_node, right=lv2_2_node)

    assert Solution.hasPathSum(self=Solution, root=root_node, targetSum=5) is False

    # test 3
    assert Solution.hasPathSum(self=Solution, root=None, targetSum=0) is False

    # test 4
    lv2_1_node = TreeNode(val=2)
    root_node = TreeNode(val=1, right=lv2_1_node)

    assert Solution.hasPathSum(self=Solution, root=root_node, targetSum=2) is False