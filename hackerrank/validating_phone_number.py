import re
for i in range(int(input())) : 
    if re.match(r'[789]\d{9}$',raw_input()): 
        print('YES') 
    else: 
        print('NO')