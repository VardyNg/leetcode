from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 0
        return False
