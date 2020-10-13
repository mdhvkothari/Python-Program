S = "cbafg"
T = "abcd"
l = []
for i in S:
    print(T.count(i))
    l.append(i*T.count(i))
    print(l)
for i in T:
    if i not in S:
        l.append(i)
print("".join(l))