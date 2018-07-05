### Write a function which asks the user for a string and prints out whether the string is a palindrome or not



def is_palindrome():
	test_palindrome = input('Give me a string and test if it is a palindrome')
	#takes string and get rid of spaces
	test_palindrome = test_palindrome.replace(' ','')
	if test_palindrome.isalpha() == True:
		#test if forward string is same as reverse string san spaces
		make_reverse = test_palindrome[::-1]
		if make_reverse.lower() == test_palindrome.lower():
			print('It is a palindrome!')
		else:
			print('It is not a palindrome')
	else:
		test_palindrome = list(test_palindrome)
		to_pop = list()
		for item in test_palindrome:
			if item.isalpha()==False:
				to_pop.append(test_palindrome.index(item))
		to_pop.reverse()
		for p in to_pop:
			test_palindrome.pop(p)
		new_test = ''.join(test_palindrome)
		make_reverse = new_test[::-1]
		if make_reverse.lower() == new_test.lower():
			print('It is a palindrome!')
		else:
			print('It is not a palindrome')


def is_palindrome():
	test_palindrome = input('Give me a string and test if it is a palindrome')
	#takes string and get rid of spaces
	test_palindrome = test_palindrome.replace(' ','')
		#test if forward string is same as reverse string san spaces
	make_reverse = reverse(test_palindrome[0:])
	if make_reverse.lower() == test_palindrome.lower():
		print('It is a palindrome!')
	else:
		print('It is not a palindrome')

r'[^\w\s] #this is regular expression, the ^ is "NOT"