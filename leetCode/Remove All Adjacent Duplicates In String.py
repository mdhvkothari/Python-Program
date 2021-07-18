class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items


a = "abbaca"
s = Stack()
for i in range(0,len(a)):
    if len(s.get_stack()) == 0:
        s.push(a[i])
    else:
        last_element = s.peek()

        if last_element == a[i]:
            s.pop()
        else:
            s.push(a[i])

result = ""
for i in range(0,len(s.get_stack())):
    result += s.get_stack()[i]
print(result)

