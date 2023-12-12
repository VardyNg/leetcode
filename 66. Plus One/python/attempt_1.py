from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # loop from the end of array to the beginning
        # if the value is 9, set it to 0 and continue the loop (add 1 at index - 1)
        # otherwise, add 1 to the value and break the loop
        index = len(digits) - 1
        while index >= 0: # O(n), at worst case we will loop through the whole array
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits

            index -= 1

        # in case the 1st element is 0, meaning it was 9 and become 10
        # we insert 1 in the 1st position and shift the whole array
        if digits[0] == 0:
            digits.insert(0, 1) # O(n), as we shift the whole array with n elements
        return digits
        