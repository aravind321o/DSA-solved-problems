class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        sumd = 0
        for i in nums:
            sumd+=i
            lst.append(sumd)

        return lst

        