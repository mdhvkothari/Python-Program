class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            sum = 0
            while(num):
                sum = sum+(num%10)
                num = num//10
            num = sum
        return num