from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the strs array
        # strs = sorted(strs) # use this in leetcode
        strs = sorted(strs, key=len) # it takes O(log n)
        start = strs[0]
        end = strs[-1]

        lp = ""
        for idx in range(min(len(start), len(end))):
            if start[idx] != end[idx]:
                break
            lp += start[idx]

        return lp
