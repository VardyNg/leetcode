from attemp_1 import Solution

def test_attemp_1():
    # test 1
    nums = [2,7,11,15]
    target = 9

    res = Solution.twoSum(self=Solution, nums=nums, target=target)

    assert res in [[0,1], [1,0]]

    # test 2
    nums = [3,2,4]
    target = 6

    res = Solution.twoSum(self=Solution, nums=nums, target=target)

    assert res in [[1,2], [2,1]]

    # test 3
    nums = [3,3]
    target = 6

    res = Solution.twoSum(self=Solution, nums=nums, target=target)

    assert res in [[0,1], [1,0]]
    