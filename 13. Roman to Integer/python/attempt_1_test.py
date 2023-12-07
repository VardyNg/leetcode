from attempt_1 import Solution

def test_attempt_1():
    # test 1
    s = "III"

    res = Solution.romanToInt(Solution, s=s)

    assert res == 3

     # test 2
    s = "LVIII"

    res = Solution.romanToInt(Solution, s=s)

    assert res == 58

    # test 3
    s = "MCMXCIV"

    res = Solution.romanToInt(Solution, s=s)

    assert res == 1994
