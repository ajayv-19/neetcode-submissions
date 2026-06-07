from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0) 
        
        heap = []
        for ele, cnt in count.items():
            heapq.heappush(heap, [cnt,ele])
            if len(heap)> k:
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         heap = []
#         for num in count.keys():
#             heapq.heappush(heap, (count[num], num))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])
#         return res
        
"""        
count the frequency of the items and store in an dictonary [element:count]

create an empty heap and add the values [-value,key] in the heap, 




"""