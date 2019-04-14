def ex1():
	count = 0
	for i in range(2, 5000):
		if i % 3 == 0 or i % 7 == 0 or i % 11 == 0:
			count += 1
	return count

if __name__ == '__main__':
	print(ex1())	
