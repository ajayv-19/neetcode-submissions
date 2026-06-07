from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r ,n= 0, len(nums) - 1,nums[0]
        
        while l < r:
            m = l + (r - l) // 2  # Find middle element
            
            # If mid is greater than the rightmost element, min is on the right side
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m  # Keep m in the search since it could be the minimum
        
        return nums[l]  # When loop exits, l == r at the minimum element
