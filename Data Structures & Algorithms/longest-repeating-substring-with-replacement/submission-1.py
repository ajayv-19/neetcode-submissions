# class Solution:
#     def characterReplacement(self, s: str, c: int) -> int:
#         left = 0
#         right = 0
#         hashing = {"":0}
#         max_element=""
#         max_len = 0
#         while right < len(s):
#             hashing[s[right]] = hashing.get(s[right],0)+1
#             if hashing[s[right]] > hashing[max_element]:
#                 max_element = s[right]
#             if right-left+1 > hashing[max_element]+c:
#                 hashing[s[left]] -=1
#                 left+=1
#             else:
#                 max_len = max(max_len, right-left+1)
#             right = right+1
#         return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res           






"""
k = 2
what if k >len(s) - > len(s)
        [] return 0

        k = 0
        a        1
k =2    c b ackar k     5
        accaccccc   9 
        aaaaaaaa.   8
        akckccccck

max_width
start = 0
firstnonindex = -1

        start with first (a) same elemsnt increse count
        non occurance set index , decrease k 

        once another non elemnt and k = 0 
             compare the start and the current index diif and max
        
        satrt = firstnonindex
        firstnonindex = -1

        if any elemnt from left tounch the end then mo need to calculate the next elemnts

"""    







        