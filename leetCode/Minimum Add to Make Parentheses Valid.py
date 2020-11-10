bal = 0
ans = 0
s = "()))(("
for i in s:
    if i == "(":
        bal+=1
    else:
        bal+=-1
    if bal == -1:
        ans+=1
        bal+=1
print(ans+bal)