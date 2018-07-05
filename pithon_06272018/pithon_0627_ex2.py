### 2. Write a function which takes a sentence as input and returns the reverse order of the words. ie "these are words" --> "words are these". Bonus: Capitalize the the first letter of the first word and end the returned string with the same punctuation as the input string. ie "these are words!" --> "Words are these!"


def rev_sent():
	sent = input('Sentence to reverse').lower()
	if sent[-1].isalpha() == True: #if there is no punctuation
		rev_sent = sent.split()[::-1]
		rev_sent[0] = rev_sent[0].capitalize() #make first word cap
		print(' '.join(rev_sent))
	else:
		punct = sent[-1]
		sent = sent.replace(punct, '')
		rev_sentlist = sent.split()[::-1]
		rev_sentlist[0] = rev_sentlist[0].capitalize()
		print(' '.join(rev_sentlist) + punct)
	
## flaw if the last character is a number. 
## use string punctuation

import string
string punctuation

#if sent[-1] in string punctuation:
