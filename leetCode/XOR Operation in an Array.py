class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arrLen=0
        i=0
        xor=0
        while(arrLen!=n):
            val = start+2*i
            xor = xor ^ val
            arrLen+=1
            i+=1
        return xor
            
        