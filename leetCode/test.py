S = "ab#c"
T = "ad#c"

def build(S):
    ans =[]
    for c in S:
        if c != '#':
            ans.append(c)
        elif ans:
            ans.pop()
        return "".join(ans)
    print(build(S) == build(T))