from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        print("containsNearbyDuplicate: ", nums)
        # we use hashmap here
        # loop through the nums and store element of nums and the index
        # in each loop, check if the element is already in the hashmap
        # if it doesn't, just add a new entry
        # if it does, check if the existing entry's index difference is within k
        #   if it does, that's a duplication
        #   otherwise, replace the entry with the current entry

        hashmap = {}

        for idx, num in enumerate(nums):
            if num in hashmap and abs(idx - hashmap[num]) <= k:
                return True

            hashmap[num] = idx

        return False
