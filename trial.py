from collections import Counter
import re

def get_iterations(str1, str2):
	print(str1)
	for i in range(len(str2)):
		if str1[i] == str2[i]:
			print(str1)

		else:
			str1 = list(str1)
			str2 = list(str2)
			str1[i] = str2[i]
			str1 = "".join(str1)
			str2 = "".join(str2)
			print(str1)



s = "Let me not to the marriage of true minds \nAdmit impediments, love is not love \nWhich alters when it alteration finds, \nOr bends with the remover to remove. \nO no, it is an ever fixèd mark \nThat looks on tempests and is never shaken; \nIt is the star to every wand'ring bark, \nWhose worth's unknown although his height be taken. \nLove's not time's fool, though rosy lips and cheeks \nWithin his bending sickle's compass come, \nLove alters not with his brief hours and weeks, \nBut bears it out even to the edge of doom: \nIf this be error and upon me proved, \nI never writ, nor no man ever loved."


s = s.lower()
words = re.findall("[a-zA-Z']+", s)
c = Counter(words)
l=[]
len_words = []

for i in words:
	l+=list(i.lower())
	len_words.append(len(i))

char_count = Counter(l)

print('1. Count the occurrences of each letter4 in the text.')
for i in char_count:
	print(i, ':', char_count.get(i))


print('\n\n2. Print the number of one-letter, two-letter, three-letter words and so on.')
len_words_count = Counter(len_words)
print('length', ':', 'count')
for i in len_words_count:
	print(i,':', len_words_count.get(i))

print('\n\n3. Print the number of occurrences of each different word in the text.')
count_words = Counter(words)
for i in count_words:
	print(i, ':', count_words.get(i))


print('\n\nPart 2: Doublets')
l1 = ['HEAD','FLOUR', 'CHAOS', 'TEARS', 'WITCH', 'BLACK', 'SLEEP', 'RIVER']
l2 = ['TAIL', 'BREAD', 'PEACE', 'SMILE', 'FAIRY', 'WHITE', 'DREAM', 'SHORE']

for i in range(len(l1)):
	print('\n')
	print(i,'.', l1[i], '-', l2[i])
	get_iterations(l1[i], l2[i])

print("Extra Pairs from document: ")
print('1. PYTHON - COURSE')
get_iterations('PYTHON', 'COURSE')

print('\n2. GIVEN - WORDS')
get_iterations('GIVEN', 'WORDS')

print('\n3. STUDENT - ARAVIND')
get_iterations('STUDENT', 'ARAVIND')