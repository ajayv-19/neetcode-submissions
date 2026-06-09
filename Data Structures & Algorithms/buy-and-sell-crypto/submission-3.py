class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit =  prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        return maxP
        # if len(prices) <2:
        #     return 0
        # left, right =0, 1
        # for i in range(1, len(prices)):
        #     if prices[i] >= prices[right]:
        #         right = i
        # for i in range(0, right):
        #     if prices[i] < prices[left]:
        #         left = i
        # return prices[right]-prices[left] if prices[right]-prices[left] > 0 else 0
        
"""
question 
1 will there be minimun 2 elements
what to do when only1 element or null array


cases to consider

1. continous decrease no profit make ( )
edge case - based on comparision even if the left is moved because its less, we cannot get positive difference


main things to verify 

1. if null cases and base cases ( eg less that required lenth case addded)
2. is output returned
3. Is returned in correct format

Things to think when coming with solugion of thinking edge cases

1. null 
2. is sorted
3. is number repeated 
4. same number is future what to conider for this problem inut 


- prices=[2,1,2,1,0,1,2] so we added >=
if prices[i] >= prices[right]:
                right = i

"""

