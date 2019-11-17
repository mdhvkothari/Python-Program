N = int(input())
customer =[]
profit=[]

for i in range(N):
    customer_element= int(input())
    customer.append(customer_element)

customer.sort()

for j in range(N):
    profit_element = customer[j]*(N-j)
    profit.append(profit_element)

print(max(profit))