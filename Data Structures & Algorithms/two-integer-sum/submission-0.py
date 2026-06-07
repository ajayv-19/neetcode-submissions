class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing = {}
        for i, n in enumerate(nums):
            if n in hashing:
                return [hashing[n],i]
            else:
                hashing[target-n] = i



"""
if sorted can use the two pointer approach"
if not sorted then use the hasing and store diifeence and index in that
"""