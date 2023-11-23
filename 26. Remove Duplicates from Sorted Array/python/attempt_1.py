from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print("removeDuplicates")

        # loop through the nums
        # if the element has appeared on the hash map, remove it from the array
        # otherwise, add the element to the hash map

        hashmap = {}
        indices = []

        # create a list of index that are to be removed (duplicates)
        for index, num in enumerate(nums):
            print("index: ", index)
            if num in hashmap:
                indices.append(index)
            else:
                hashmap[num] = 0

        print("indices: ", indices)
        # Remove the element by index in indices
        # sort and reverse the indices array to avoid shifting the array when removing element in loop
        # example: indices = [5,6,4,2,9]
        # sorted: indices = [2,4,5,6,9]
        # reversed: indices = [9,6,5,4,2]
        # then we can remove the element from the end of array!
        for index, value in enumerate(reversed(sorted(indices))):
            print("value: ", value)
            nums.pop(value)

        print("nums: ", nums)
        return len(nums)
