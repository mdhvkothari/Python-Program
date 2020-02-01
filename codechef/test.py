T = int(input())
for _ in range(T):
    N = int(input())
    question=[]
    score=[]
    result=[]
    remaining=[]
    for _ in range(N):
        q,p = map(int,input().strip().split(" "))
        if(q<=8):
            question.append(q)
            score.append(p)
            remaining.append(p)
    for i in range(0,len(question)):
        for j in range(i,len(question)):
            if(question[i]==question[j]):
                if(score[i]>score[j]):
                    result.append(score[i])
                    remaining.append(score[i])
                elif(score[i]<score[j]):
                    result.append(score[j])
                    remaining.append(score[j])
    
    print(remaining)
