import math
def get_divisors(num):
	return [i for i in range(1, num) if num % i == 0]

def sum_divisors(num):
	return sum(get_divisors(num))

def abundance(num):
	return sum_divisors(num) - num	

def ex7():
	sum = 0
	for i in range(1000, 10001):
		save = abundance(i)
		if abundance(i) > 0:
			sum += save
	return sum

if __name__ == '__main__':
	print(ex7())
