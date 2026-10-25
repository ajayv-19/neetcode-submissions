class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [1] * n
        suff = [1] * n

        pre = 1
        suf = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pre
            pre = pref[i]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suf
            suf = suff[i]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res