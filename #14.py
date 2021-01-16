# from datetime import datetime
# def collatz(n):
# 	count = 1
# 	while n != 1:
# 		if n%2 == 0:
# 			n = (n/2)
# 		else:
# 			n = ((n*3)+1)
# 		count += 1
# 	return count
# max = 0
# t1 = datetime.now()
# for i in range(2, 1000000):
# 	x = collatz(i)
# 	if x > max:
# 		max = x
# 		num = i
# t2 = datetime.now()
# print(t2-t1)



from datetime import datetime
collatz_seq = [0, 1, 2]
def collatz(n):
	count = 1
	try:
		count = collatz_seq[int(n)]
	except:
		while n != 1:
			if n%2 == 0:
				n = (n/2)
			else:
				n = ((n*3)+1)
			if int(n) <= len(collatz_seq)-1:
				count += collatz_seq[int(n)]
				# print(n, collatz_seq[int(n)])
				break
			count += 1
			# print(count, n)
		collatz_seq.append(count)
		print(collatz_seq)
	return count
max = 0
# print(collatz(3))
t1 = datetime.now()
for i in range(2, 13):
	x = collatz(i)
	if x > max:
		max = x
		num = i
t2 = datetime.now()
print(num, max)
print(t2-t1)