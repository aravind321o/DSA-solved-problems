class Solution:
    def addStrings(self, num1: str, num2: str,) -> str:
        sys.set_int_max_str_digits(50000)
        a,b=0,0
        r,s=0,0
        for i in range(len(num1)):
            r = ord(num1[i])-48
            a=a*10 + r
        for j in range(len(num2)):
            s = ord(num2[j])-48
            b=b*10 +s
        
        return str(a+b)
