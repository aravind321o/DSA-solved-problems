class Solution:
    def fib(self, n: int,m={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in m:
            return m[n]
        else:
            m[n] = self.fib(n-1)+ self.fib(n-2)
        return m[n]