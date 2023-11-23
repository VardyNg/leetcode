from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # use two pointer approach
        # given the nums has minimum of length = 1

        # there can't be a duplication when there is only on element
        if len(nums) == 1:
            return False

        # we can savely define j = 1 as the array has at least two element in this point
        j = 1

        # we sort the nums,
        # e.g. [1,2,3,1] -> [1,1,2,3]
        # then, we point i to index: 0 and j to index: 1
        # if the value in i = j, that's a duplicate
        # if not, then move i to j, then j to j + 1
        nums = sorted(nums)

        for i in range(0, len(nums)):
            # duplicate found
            print("i: ", i)
            print("j: ", j)
            print("nums[i]: ", nums[i])
            print("nums[j]: ", nums[j])

            if nums[i] == nums[j]:
                return True

            # move j to i
            j = i

        return False
    