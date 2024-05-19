class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        data = []
        res= []
        for num in nums:
            heapq.heappush(data,num)

        for i in range(len(data)):
            res.append(heapq.heappop(data))  
        return res 
        