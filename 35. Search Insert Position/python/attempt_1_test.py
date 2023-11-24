from attempt_1 import Solution

def test_attempt_1():
    # test 1
    nums = [1,3,5,6]
    target = 5

    res = Solution.searchInsert(self=Solution, nums=nums, target=target)

    assert res == 2
    
    # test 2
    nums = [1,3,5,6]
    target = 2

    res = Solution.searchInsert(self=Solution, nums=nums, target=target)

    assert res == 1
    
    # test 3
    nums = [1,3,5,6]
    target = 7

    res = Solution.searchInsert(self=Solution, nums=nums, target=target)

    assert res == 4

    # test 4
    nums = [1]
    target = 0
    
    res = Solution.searchInsert(self=Solution, nums=nums, target=target)

    assert res == 0
    
    # test 5
    nums = [1,3]
    target = 3
    
    res = Solution.searchInsert(self=Solution, nums=nums, target=target)
    
    assert res == 1
    
    # test 6
    nums = [1]
    target = 1
    res = Solution.searchInsert(self=Solution, nums=nums, target=target)

    assert res == 0
