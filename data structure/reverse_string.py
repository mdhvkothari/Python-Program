from stack import Stack

string = input()
s = Stack()
for i in range(0,len(string)):
    s.push(string[i])
reverse =""
while not s.is_empty():
    reverse += s.pop()

print(reverse)

