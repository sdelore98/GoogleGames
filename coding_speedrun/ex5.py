def ex5(str):
	alpha = 'GHIJKLMNOPQRSTUVWXYZABCDEF'
	dict = {}
	for char in str:
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] += 1
	end_str = ""
	for i in range(len(alpha)):
		if alpha[i] in dict:
			end_str += (alpha[i]*dict[alpha[i]])

	return end_str

if __name__ == '__main__':
	print(ex5('TECHCHALLENGECODINGSPEEDRUN'))
