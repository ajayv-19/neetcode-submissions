class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums,"sorted")
        result = []
        if len(nums)<3:
            return result
        for i in range(len(nums)-2):
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            # print("i",i)
            target = nums[i]
            # print("target",target)
            l , r = i+1, len(nums)-1
            # print("ls",l,"rs",r)
            while l <r:
                # print("l",l,"r",r)
                sum_val = nums[l]+nums[r]
                # print("sum_val",sum_val)
                if sum_val +target == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while (l<r and nums[l] == nums[l-1]):
                        l+=1
                    r=r-1
                elif sum_val +target >0 :
                    r=r-1
                elif sum_val +target < 0 :
                    l=l+1
        return result
                




        