from attempt_1 import Solution

def test_attempt_1():
    # test 1
    nums = [1,2,3,1]
    k = 3
    res = Solution.containsNearbyDuplicate(self=Solution, nums=nums, k=k)

    assert res is True


    # test 2
    nums = [1,0,1,1]
    k = 1
    res = Solution.containsNearbyDuplicate(self=Solution, nums=nums, k=k)

    assert res is True

    # test 3
    nums = [1,2,3,1,2,3]
    k = 2
    res = Solution.containsNearbyDuplicate(self=Solution, nums=nums, k=k)

    assert res is False
