from typing import List

class Solution:
     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        print("containsNearbyDuplicate: ", nums)
        # we use sliding windows with 2k+1 as the window size
        # slide the window from left to right, if there is a duplicate within window
        # there is a duplicate
        hashset = set()
        last_start_index = 0
        for index, num in enumerate(nums):
            print("index: ", index)
            print(hashset)
            # calculate the start_index
            start_index = max(0, index - k)
            print("start_index: ", start_index)
            print("last_start_index: ", last_start_index)
            if start_index != last_start_index: # it means the array has shifted and need to remove the previous element
                hashset.remove(nums[last_start_index])
                
            last_start_index = start_index

            # if num is in hashset, then it is a duplication
            if num in hashset:
                return True

            # add the num to the sety
            hashset.add(num)
 
        return False
