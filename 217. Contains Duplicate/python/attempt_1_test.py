from attempt_1 import Solution

def test_attempt_1():
    # test 1
    nums = [1,2,3,1]

    res = Solution.containsDuplicate(self=Solution, nums=nums)

    assert res is True


    # test 2
    nums = [1,2,3,4]

    res = Solution.containsDuplicate(self=Solution, nums=nums)

    assert res is False

    # test 3
    nums = [1,1,1,3,3,4,3,2,4,2]

    res = Solution.containsDuplicate(self=Solution, nums=nums)

    assert res is True
