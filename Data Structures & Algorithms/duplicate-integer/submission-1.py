class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for i in nums:
            
            if i in mapping:
                return True
            mapping[i]= 1
            
        return False


"""
Questions 

1. Is it sorted - (itterate ans compare next approach)
2. Are numbers in fixed range or random (total sum can be checked based on n(n+1)/2 , but not gautanteed, if multiple repetaion allowed)
3. Out of many only 1 values repeats (if so only once for multiple times) or multiple values repeat (maths approach)
(1,2,3,4,5) (3,3,3,3,3) (5,5,2,2,1) both give 15 (but only 1 elemnt 1 time repeat direct sum works)

4. using memory approach

"""


