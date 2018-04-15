 # -*- coding: utf-8 -*- 
def Quick3Way(arry,lo,hi):

	if lo>=hi:
		return 


	lt = lo 
	i = lt+1
	gt = hi

	#三路切分算法的目的在于，当数组中有重复元素的时候。可以不用再一次切分元素
	temp = arry[lo]
	while i<=gt:
		print(i)
		if arry[i]<temp:
			exch(arry,lt,i)
			lt+=1
			i+=1
		elif arry[i]>temp:
			exch(arry,i,gt)
			gt-=1
		else:
			i+=1

	#数组在一次切分好之后，再一次不断地切分
	Quick3Way(arry,lo,lt-1)
	Quick3Way(arry,gt+1,hi)

	


def exch(arry,i,j):
	if i>=j:
		return

	if arry[i]>arry[j]:
		arry[i],arry[j] = arry[j],arry[i]

		






		

if __name__ == '__main__':
	print("a")
	arry = [2, 6, 3, 1, 5, 7, 4,-1];
	Quick3Way(arry,0,len(arry)-1)
	print(arry)

	





