class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        hashing = {}
        start = 0
        for i in range(len(s)):
            if s[i] in hashing and hashing[s[i]] >= start:
                start = hashing[s[i]]+1
                hashing[s[i]] = i
            else:
                max_size = max(i-start+1, max_size)
                hashing[s[i]] = i
        return max_size





        


        