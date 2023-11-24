from typing import List
import math

# Overall idea
# Given nums = [2,5,6,7,8,9] and target = 7
# We use two pointers (start_index & end_index), initially set start_index = 0 and end_index = 6 (length of nums)
# By the two pointers, we calculate the mid_index and thus get the mid value
# Compare target with mid value, we control the pointers thus control the range
# if target is larger or equal to mid value, it means the range we search should limit to [mid: end_index]
# if target is less then mid value, we limit the range to [start_index: mid]
# then go thorugh the same process, we narrow down the range until start_index and end_index is adjacent
# i.e. end_index - start_index == 1
# then we know the end_index is the target position (this is base on the nums' element being distinct!)
# In addition, there are some conditions to handle other cases
# 1. if target is smaller or equal to the 1st elements in the array, it means target is smaller than all element in the array (Given nums is sorted)
#       then we return 0
# 2. if target is larger then the last element in the arraym it means target is larget than all element in the arry (given the array is sorted)
#       then we return the array length (last element's index + 1)

class Solution:
    
    def binarySearch(self, nums: List[int], start_index: int, end_index: int, target: int):
        print("binarySearch: start_index: ", start_index, "end_index ", end_index)

        # handle if target is not within the nums' range
        # i.e. target < nums[0] or target > nums[last index]
        if target <= nums[0]:
            return start_index
        if target > nums[-1]:
            return end_index

        # ending conditions
        # if start_index and end_index are located adjacently, i.e. their difference is 1
        # return end_index as the insert position
        if end_index - start_index == 1:
            print("return ", end_index)
            return end_index

        # calculate the mid of start_index and end_index and ceil it
        # e.g. (5+10)/2 -> 7.5 -> 8
        mid = math.ceil((start_index+end_index)/2)
        print("mid: ", mid)
        mid_value = nums[mid]
        print("mid_value: ", mid_value)

        # if target > mid_value, move start_index to mid
        if mid_value < target:
            print("mid_value < target")
            return self.binarySearch(self, nums, mid, end_index, target)
            # TODO: sort out why leetcode's python3 doesn't need to pass self
            # use this above in leetcode...
            # return self.binarySearch(nums, mid, end_index, target)

        # if target <= mid_value, move end_index to mid
        if mid_value >= target:
            print("mid_value >= target")
            return self.binarySearch(self, nums, start_index, mid, target)


    def searchInsert(self, nums: List[int], target: int) -> int:
        print("\nsearchInsert")
        # we use binary search here
        return self.binarySearch(self, nums, 0, len(nums), target)
