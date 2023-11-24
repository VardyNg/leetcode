from attempt_1 import Solution

def test_attempt_1():
    # test 1
    digits = [1,2,3]
    expected = [1,2,4]
    
    res = Solution.plusOne(self=Solution, digits=digits)
    
    assert res == expected
    
    # test 2
    digits = [4,3,2,1]
    expected = [4,3,2,2]
    
    res = Solution.plusOne(self=Solution, digits=digits)
    
    assert res == expected
    
    # test 3
    digits = [9]
    expected = [1,0]
    
    res = Solution.plusOne(self=Solution, digits=digits)
    
    assert res == expected
    
    # test 4
    digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
    expected = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,4]
    
    res = Solution.plusOne(self=Solution, digits=digits)
    
    assert res == expected