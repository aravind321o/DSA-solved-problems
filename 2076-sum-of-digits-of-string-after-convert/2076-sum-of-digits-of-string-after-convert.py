class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numericstr = ""
        for ch in s:
            numericstr += str(ord(ch)- ord("a")+1)

        while k>0:
            digisum = 0
            for num in numericstr:
                digisum += int(num)
                numericstr = str(digisum)
            k-=1    
        
        return int(digisum)