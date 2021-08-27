class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(l):
            rem = []
            for i in l:
                if i != '#':
                    rem.append(i)
                elif rem:
                    rem.pop()    
            return "".join(rem)
        return check(s) == check(t)
                
        