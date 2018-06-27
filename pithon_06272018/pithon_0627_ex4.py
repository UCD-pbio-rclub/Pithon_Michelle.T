birthday = {
	'Michelle Tang' : '01/16/1990',
	'Barack Obama' : '08/04/1961',
	'Ellen DeGeneres' : '01/26/1958',
	'Barbara McClintock' : '06/16/1902'}

def give_birthday():
	print('Welcome to the birthday dictionary. We know the birthdays of:', list(birthday))
	birth_lookup = input('Who\'s birthday do you want to look up?')
	print('The birthday of', birth_lookup,'is', birthday[birth_lookup])
