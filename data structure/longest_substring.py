a="abcabcbb"
seen ={}
start= 0
max_length =0
for i in range(0,len(a)):
    if a[i] in seen:
        start = max(start,seen[a[i]]+1)
        print(seen)
        print(-start)
    seen[a[i]] = i
    max_length = max(max_length,i-start+1)
    print(max_length)

print(max_length)
