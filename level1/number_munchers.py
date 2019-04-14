def magic_duo(num1, num2):
	product = str(num1 * num2)
	for i in range(len(product) - 1):
		if int(product[i]) >= int(product[i+1]):
			return False
	return True
	
def number_munchers():
	num = 0
	dict = []
	for i in range(1, 1000):
		for j in range(1, i + 1):
			if i * j < 1000:
				if magic_duo(i, j) and (i, j) not in dict and (j, i) not in dict:
					num += 1
					dict += (i, j)
	return num
		
if __name__ == '__main__':
	print(number_munchers())
