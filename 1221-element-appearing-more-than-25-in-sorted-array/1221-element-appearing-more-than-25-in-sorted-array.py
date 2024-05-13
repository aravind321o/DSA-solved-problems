class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        n=len(arr)
        for keys, values in count.items():
            if values>n/4:
                return keys
        