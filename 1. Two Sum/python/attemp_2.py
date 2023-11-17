from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Sort the array and maintain its own indexes using tuples
        # the enumerate(nums) will create a tuple of index and value (index, value)
        # the key indicate sort by x[1] i.e. the actual value
        # e.g. [3,2,4] -> [(1, 2), (0, 3), (2, 4)]
        print(nums)
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        print(nums)
        
        left = 0
        right = len(nums) - 1

        while True:
            print("=======")
            print("left: ", left)
            print("right: ", right)
            print("nums[i] ", nums[left][1])
            print("nums[j] ", nums[right][1])

            two_sum = nums[left][1] + nums[right][1]
            print("two_sum: ", two_sum)

            if two_sum > target:
                # move right pointer to the left
                print("two_sum > target")
                right -= 1
            elif two_sum < target:
                # move left pointer to the right
                print("two_sum < target")
                left += 1
            else:
                # return the actual index in the tuple
                # e.g. if left = 0 and right = 2 & nums = [(1, 2), (0, 3), (2, 4)]
                # the left and right pointers are pointing (1,2) and (2,4) respectively
                # their actual index is the 1st element, which is 1 and 2 in this case
                # thereforethe actual return should be [1, 2] <- (1,2)[0], (2,4)[0]
                print("return: ", [nums[left][0], nums[right][0]])
                return [nums[left][0], nums[right][0]]
            