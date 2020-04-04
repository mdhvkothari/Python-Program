class Stack():
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()
    
    def is_empty(self):
        if(item.lenght()==0):
            print('Stack is empty')
        

    def peek(self):
        return self.item[-1]

    def show(self):
        return self.item 



s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.show())
s.pop()
print(s.show())
print(s.peek())

