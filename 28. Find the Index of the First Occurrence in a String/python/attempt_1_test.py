from attempt_1 import Solution

def test_attempt_1():
    # test 1
    haystack = "sadbutsad"
    needle = "sad"
    
    res = Solution.strStr(self=Solution, haystack=haystack, needle=needle)
    
    assert res == 0
    
    # test 2
    haystack = "leetcode"
    needle = "leeto"
    
    res = Solution.strStr(self=Solution, haystack=haystack, needle=needle)
    
    assert res == -1

    # test 3
    haystack = "a"
    needle = "a"
    
    res = Solution.strStr(self=Solution, haystack=haystack, needle=needle)
    
    assert res == 0
    
    # test 4
    haystack = "abc"
    needle = "c"
    
    res = Solution.strStr(self=Solution, haystack=haystack, needle=needle)
    
    assert res == 2