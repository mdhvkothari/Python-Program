class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        count= 0
        while(n/i>=1):
            count += int(n/i)
            i *= 5
        return count