from attempt_2 import Solution

def test_attempt_2():
    # test 1
    strs = ["flower","flow","flight"]

    res = Solution.longestCommonPrefix(Solution, strs=strs)

    assert res == "fl"

    # test 2
    strs = ["dog","racecar","car"]

    res = Solution.longestCommonPrefix(Solution, strs=strs)

    assert res == ""

    # test 3
    strs = ["dog","dog","dog"]

    res = Solution.longestCommonPrefix(Solution, strs=strs)

    assert res == "dog"

    # test 4

    strs = ["abc"]

    res = Solution.longestCommonPrefix(Solution, strs=strs)

    assert res == "abc"

    # test 5
    
    strs = ["ab", "a"]
    
    res = Solution.longestCommonPrefix(Solution, strs=strs)

    assert res == "a"