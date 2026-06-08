class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashing = {}
        for i in nums:
            if i not in hashing:
                hashing[i] = 1
        max_c = 0
        for k in hashing.keys():
            val = k
            c = 0
            while hashing.get(k,0)>0:
                c+=1
                k+=1
            max_c = max(max_c, c)
        return max_c       

        