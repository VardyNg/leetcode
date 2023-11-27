
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # we use sliding window with size = length of needle
        # e.g. haystack = "leetcode" and "needle" = "leetco"
        # window_size = 5, haystack_length = 8
        # the initial window will be "leetc"
        # we loop from "l" (0) to "t" (haystack_length - window_size = 3)
        # we construct the window in each loop,
        # by remove the 1st char and append the next char

        window_size = len(needle)
        haystack_length = len(haystack)
        print("window_size: ", window_size)
        print("haystack_length: ", haystack_length)

        window = haystack[0: window_size]
        print("initial window: ", window)

        print(range(0, haystack_length - window_size + 1))
        for index in range(0, haystack_length - window_size + 1):
            print(index, window)
            if window == needle:
                return index
            if index == haystack_length - window_size:
                continue

            window = window[1:] + haystack[window_size + index]
        return -1
            