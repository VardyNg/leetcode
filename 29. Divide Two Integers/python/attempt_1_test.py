from attempt_1 import Solution

def test_attempt_1():
    # test 1
    dividen = 10
    divisor = 3

    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 3

    # test 2
    dividen = 7
    divisor = -3

    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == -2
    
    # test 3
    dividen = 0
    divisor = 10
    
    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 0
    
    # test 4
    dividen = 1
    divisor = 10
    
    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 0
    
    # test 5
    dividen = 1
    divisor = 1
    
    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 1
    
    # test 6
    dividen = -2147483648
    divisor = -1
    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 2147483647
    
    # test 7
    dividen = 2147483644
    divisor = 2
    assert Solution.divide(self=Solution, dividend=dividen, divisor=divisor) == 1073741822