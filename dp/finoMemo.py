#here we are storing results into an arr so that no need to calculate fibo again and again


def finoMemo(n,arr):
    #base case
    if n == 0 or n == 1:
        return n

    #check wether fib(n) result in arr or not
    if arr[n] != 0:
        return arr[n]

    a = finoMemo(n-1,arr) + finoMemo(n-2,arr)

    arr[n] = a

    return a


arr = []
num = 10
for i in range(0,11):
    arr.append(0)

print(finoMemo(num,arr))