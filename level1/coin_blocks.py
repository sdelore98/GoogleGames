def coin_blocks():
	sum = 0
	for i in range(1, 1001):
		if i % 15 == 0:
			sum += (i * 10)
		elif i % 3 == 0:
			sum += (i * 2)
		elif i % 5 == 0:
			sum += (i * 3)
		else:
			sum += i
	return sum		

if __name__ == '__main__':
	print(coin_blocks())
