english_number=int(input())
english_student=list(map(int,raw_input().strip().split(' ')))
french_number=int(input())
french_student=list(map(int,raw_input().strip().split(' ')))
total=[]
for i in range(0,french_number):
	a=0
	while(a<=len(english_student)-1):
		if english_student[a]==french_student[i]:
			total.append(french_student[i])

		a+=1
print(len(total))






















