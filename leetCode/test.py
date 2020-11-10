S = "a-bC-dEf-ghIj"
letter = []
ans = []
for  i  in range(0,len(S)):
    if S[i].isalnum():
        letter.append(S[i])
for i in S:
    if i.isalpha():
        ans.append(letter.pop())
    else:
        ans.append(i)

print ("".join(ans))