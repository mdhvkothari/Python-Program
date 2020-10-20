words = ["gin", "zen", "gig", "msg"]
con = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dic = {}
for i in range(0,len(con)):
    dic[alp[i]] = con[i]

sym=[]
for i in range(0,len(words)):
    sym1=""
    for j in range(0,len(words[i])):
        sym1+=dic[words[i][j]]
    sym.append(sym1)
print(len(set(sym)))