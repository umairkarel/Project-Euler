# def Abundants(n):
# 	abundants = set()
# 	for i in range(1, n):
# 		sum = 1
# 		for j in range(2, int(i**0.5)+1):
# 			if (i % j == 0) : 
# 				sum += j
# 				if j!=i//j:
# 					sum += i // j
                  
# 		if sum > i:
# 			abundants.add(i)
# 	return abundants
# a = list(sorted(Abundants(28124)))

# def sumofAb(n):
# 	for i in range(1, n+1):
# 		if a.count(i) and a.count(n-i):
# 			return True
# 	return False

# ans = []
# print()
# for i in range(1, 28124):
# 	if not sumofAb(i):
# 		ans.append(i)
# print(ans)

