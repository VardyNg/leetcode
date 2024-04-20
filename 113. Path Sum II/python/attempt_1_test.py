from attempt_1 import Solution
from TreeNode import TreeNode

def test_attempt_1():
    # test 1
    lv4_node_1 = TreeNode(val=7)
    lv4_node_2 = TreeNode(val=2)

    lv4_node_3 = TreeNode(val=5)
    lv4_node_4 = TreeNode(val=1)

    lv3_node_1 = TreeNode(val=11, left=lv4_node_1, right=lv4_node_2)
    lv3_node_2 = TreeNode(val=13)
    lv3_node_3 = TreeNode(val=4, left=lv4_node_3, right=lv4_node_4)

    lv2_node_1 = TreeNode(val=4, left=lv3_node_1)
    lv2_node_2 = TreeNode(val=8, left=lv3_node_2, right=lv3_node_3)

    root = TreeNode(val=5, left=lv2_node_1, right=lv2_node_2)

    assert Solution.pathSum(self=Solution, root=root, targetSum=22) == [[5,4,11,2],[5,8,4,5]]

    # test 2
    l2_node_1 = TreeNode(val=2)
    l2_node_2 = TreeNode(val=3)
    root = TreeNode(val=1, left=l2_node_1, right=l2_node_2)

    assert Solution.pathSum(self=Solution, root=root, targetSum=5) == []

    # test 3
    l2_node_1 = TreeNode(val=2)
    root = TreeNode(val=1, left=l2_node_1)

    assert Solution.pathSum(self=Solution, root=root, targetSum=0) == []
    
    # test 4
    l2_node_1 = TreeNode(val=2)
    root = TreeNode(val=1, left=l2_node_1)

    assert Solution.pathSum(self=Solution, root=root, targetSum=1) == []