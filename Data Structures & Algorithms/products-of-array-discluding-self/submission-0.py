class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0]* len(nums)
        presum = 1
        for i in range(len(nums)):
            out[i] = presum
            presum = presum* nums[i]
        postsum = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] = out[i] * postsum
            postsum = postsum* nums[i]
        return out


        