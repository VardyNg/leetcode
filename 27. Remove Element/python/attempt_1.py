from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we iterate through the nums array
        # use index to point the position in array
        # we limit the index by max_index, which value will reduce when the array size changes
        max_index = len(nums) - 1
        index = 0
        while index <= max_index: # O(n)
            # Do not move index if there is a match
            # As the same index position will become the next value with array.pop
            if nums[index] == val:
                max_index -= 1
                nums.pop(index) # O(n)
            else:
                index += 1

        return len(nums)
