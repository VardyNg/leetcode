from typing import List
import math

class Solution:
    
    def binarySearch(self, nums: List[int], start_index: int, end_index: int, target: int) -> int:
        if start_index == end_index:
            return start_index
        
        mid = (start_index + end_index) // 2
        mid_value = nums[mid]

        if target == mid_value:
            return mid
        elif target < mid_value:
            return self.binarySearch(self, nums, start_index, mid, target)
        else:
            return self.binarySearch(self, nums, mid + 1, end_index, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(self, nums, 0, len(nums), target)