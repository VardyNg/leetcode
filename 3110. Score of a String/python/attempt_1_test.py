from attempt_1 import Solution

def test_attempt_1():
    # test 1
    s = "hello"
    assert Solution.scoreOfString(self=Solution, s=s) == 13
    
    # test 2
    s = "zaz"
    assert Solution.scoreOfString(self=Solution, s=s) == 50