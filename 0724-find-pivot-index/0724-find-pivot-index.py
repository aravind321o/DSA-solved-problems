class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml=0
        sumr=0
        total = sum(nums)
        
        
        for i in range(len(nums)):
            sumr = total - suml - nums[i]
            
            if sumr == suml:
                return i
            
            suml+=nums[i]
        
        return -1