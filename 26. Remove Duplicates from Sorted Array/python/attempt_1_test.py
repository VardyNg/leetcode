from attempt_1 import Solution

def test_attempt_1():
    # test 1
    nums = [1,1,2]
    expected_nums = [1,2]

    k = Solution.removeDuplicates(self=Solution, nums=nums)

    assert k == len(expected_nums)
    for i in range(0, len(nums)):
        assert nums[i] == expected_nums[i]


    # test 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected_nums = [0,1,2,3,4]
    
    k = Solution.removeDuplicates(self=Solution, nums=nums)

    assert k == len(expected_nums)
    for i in range(0, len(nums)):
        assert nums[i] == expected_nums[i]

    # test 3
    nums = [1,2,2]
    expected_nums = [1,2]
    
    k = Solution.removeDuplicates(self=Solution, nums=nums)

    assert k == len(expected_nums)
    for i in range(0, len(nums)):
        assert nums[i] == expected_nums[i]