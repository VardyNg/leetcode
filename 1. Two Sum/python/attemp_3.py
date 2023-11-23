from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        # Since A + B = target
        # Then: minuend (target) - subtrahend (A) = difference (diff) (B)
        # We will 1st calculate the diff by A and diff
        # Then find if the hash map has a key of diff (B)
        # if it does, it means A + B = target
        # We found the two indices!

        for index, num in enumerate(nums):
            # as the question implies that the number in nums are unique
            # therefore we can savely use the number as map's key

            diff = target - num
            print("index: ", index)
            print("diff: ", diff)

            # if the diff exist in the hash map
            # it means we have found the solution
            if diff in hashmap:
                return [index, hashmap[diff]]

            # otherwise, add the current index to key: num
            # num: index
            hashmap[num] = index

            print(hashmap)
