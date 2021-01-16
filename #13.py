sum = 0
with open('nums.txt') as nums:
	for num in nums:
		sum += int(num)
print(sum)