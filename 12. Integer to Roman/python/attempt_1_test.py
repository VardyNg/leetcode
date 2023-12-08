from attempt_1 import Solution

def test_attempt_1():
    # test 1
    num = 3
    
    res = Solution.intToRoman(Solution, num=num)
    
    assert res == "III"
    
    
    # test 2
    num = 58
    
    res = Solution.intToRoman(Solution, num=num)
    
    assert res == "LVIII"
    
    
    # test 1
    num = 1994
    
    res = Solution.intToRoman(Solution, num=num)
    
    assert res == "MCMXCIV"
    