import re
n=int(input())
for i in range(0,n):
    name,email = raw_input().split(' ')
    checker = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>',email)
    if checker:
        print name,email