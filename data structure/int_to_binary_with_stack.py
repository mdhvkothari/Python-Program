from stack import Stack

def int_to_bianry(number):
    s = Stack()
    while(number>0):
        remainder  = number%2
        s.push(remainder)
        number = number//2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(int_to_bianry(242))

