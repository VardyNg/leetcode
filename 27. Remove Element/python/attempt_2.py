from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # as the question on evaluate the 1st k element, that mean we don't care about the last l element (l = remaining elements)
        # we iterate through the array with an external index
        # in the iteration, if an element doesn't match val, we assign that element at position = index, and incrase index by 1

        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index
