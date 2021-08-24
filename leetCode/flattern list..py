def flatten(S):
    if S == []:
        return S

    if isinstance(S[0], list):
        print(flatten(S[0]) + flatten(S[1:]))
        return flatten(S[0]) + flatten(S[1:])

    return S[:1] + flatten(S[1:])
s=[3,5,[[7]],[[[8]]],[1,2]]
print("Flattened list is: ",flatten(s))