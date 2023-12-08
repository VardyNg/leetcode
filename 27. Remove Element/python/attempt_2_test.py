from attempt_1 import Solution

def test_attempt_1():
    # test 1
    nums = [3,2,2,3]
    val = 3
    res = Solution.removeElement(Solution, nums=nums, val=val)
    print(nums)
    assert res == 2

    # test 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(nums)
    res = Solution.removeElement(Solution, nums=nums, val=val)

    assert res == 5