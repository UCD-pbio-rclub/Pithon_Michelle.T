# can calculate time required to process code with time.time()
t0 = time.time()


### Exercise 1
### A for loop that prints the first 100 numbers of the Fibonacci series

first_val = 0
second_val = 1

for fib_n in range(0,100):
	if(fib_n <=1):
		new_fib = fib_n
	else:
		new_fib = first_val + second_val
		first_val = second_val
		second_val = new_fib
	print(new_fib)


### Excercise 2
### Using the randome module and the examples in the book, simulate 1000 random single die throws the print the proportion of odd numbered dice throws
### Optional: repeat using 3 dice in each throw and the sum of dice

import random

odd_throws = 0

for x in range(1000):
	random_number = random.randint(1,6)
	print(random_number)
	if random_number%2 != 0:
		odd_throws = odd_throws + 1

print ('Proportion of odd throws is', float(odd_throws)/1000)


### Excercise 3
### Use a while loop to print the first 100 prime numbers

new = 1
n = 1

while n < 100:
	new = new + 1
	if new%2==0 or new%3==0 or new%5==0 or new%7==0:
		print ""
	else:
		n = n + 1
		print new

### missed the prime numbers less than 11

## john's example
total = 0
i = 2


while total < 100:
	for x in range(2,i):
		if (i % x) == 0:
			break
		else:
				total += 1
				if (total == 100):
					print(i)
				else:
					print( i, end = ", ")
		i += 1


### Exercise 4
### Using the following parameters, state whether the call evaluates to True or False and why

w = 3
x = 10
y = 5
z = 7

 #a) w > z - 2 FALSE 3 is not greater than 7-2 (5)
 #b) 1 + x / y == w TRUE 1 + 10/5 (2)
 #c) y / w <= 1.66 TRUE 5/3 is approximately 1.66



### Exercise 5
###Give an example of the following
 legal_name			#   a) A conventional legal variable name
 This_is_also_Legal #   b) A non-conventional legal variable name
 3notlegal			#   c) A  non-conventional illegal variable name


