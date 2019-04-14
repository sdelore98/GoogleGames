def ex4():
	nums = [3, 2, 4, 6, 3, 4, 5, 8, 6, 7, 9, 6, 3, 6, 8, 4, 2, 2, 4, 6, 2, 1, 3, 4, 5, 6, 7, 4, 5, 7, 4, 5, 3, 2, 5, 6, 3, 7, 8, 3, 2, 9, 0, 4, 3, 6, 8, 9]
	dict = {}
	for num in nums:
		if num not in dict:
			dict[num] = 1
		else:
			dict[num] += 1
	count = 0
	for item in dict:
		if dict[item] % 2 == 1:
			count += 1
	return count

if __name__ == '__main__':
	print(ex4())	
