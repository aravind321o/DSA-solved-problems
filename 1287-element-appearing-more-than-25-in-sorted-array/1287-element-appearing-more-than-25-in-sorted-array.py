class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        total = len(arr)
        quater = total * 0.25
        temp= arr[0]
        count = 1

        for i in range(1,total):
            if arr[i] == temp:
                count +=1
                if count> quater :
                    
                    break
            else:
                temp = arr[i]
                count = 1
        return temp
        