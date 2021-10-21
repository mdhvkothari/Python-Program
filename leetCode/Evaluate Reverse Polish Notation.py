def compute(operations,stack):
    num1 = stack.pop()
    num2 = stack.pop()

    if operations == '*':
        result = num1*num2
    elif operations == '/':
        result = int(num2/num1)
    elif operations == '+':
        result = num1+num2
    elif operations== '-':
        result = num2-num
    stack.append(result)


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
operation = ['*','/','+','-']
stack = []
result=0
for i in tokens:
    if i in operation:
        compute(i,stack)
    else:
        stack.append(int(i))


    print(stack)






