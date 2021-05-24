list1 = [10,20,30,40,50]
list2 = [3,7,16,43,67,78,85]
def mergeLists(list1,list2,list3=[],index1=0,index2=0):
  
	'''
	Objective 			: To merge tow sorted lists into third list.
	Input Parameters	:
				list1	: First List
				list2 	: Second List
				list3	: default - empty list.
				index1	: default 0 - for iterating list1
				index2	: default 0 - for iterating list2
	Return Values		: List3, after merging list1 and list2
	'''
  
	#Approach			: Recursion is used.

	if index1 == len(list1) and index2 == len(list2):
		return list3
	elif index1 == len(list1) or index2 == len(list2):
		if index1 == len(list1):
			list3 = list3 + list2[index2:]
			return list3
		else:
			list3 = list3 + list1[index1:]
			return list3
	elif list1[index1] > list2[index2]:
		list3.append(list2[index2])
		index2 += 1
		return mergeLists(list1,list2,list3,index1,index2)
	elif list1[index1] < list2[index2]:
		list3.append(list1[index1])
		index1 += 1
		return mergeLists(list1,list2,list3,index1,index2)

print('List 1 is ',list1)
print('List 2 is ',list2)
finalList = mergeLists(list1,list2)
print('Final merged list is ',finalList)
