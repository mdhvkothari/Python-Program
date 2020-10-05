N = 5
binary = bin(N)
binary = list(binary[2:])
for i in range(0,len(binary)):
    if binary[i] == "0":
        binary[i] = "1"
    else:
        binary[i] = "0"
binary = "".join(binary)
print(int(binary,2))

