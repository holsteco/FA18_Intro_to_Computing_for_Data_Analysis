#corey b. holstege
#2018-08-29
#http://interactivepython.org/runestone/static/thinkcspy/Labs/lab12_01.html

def countA(text):
	count = 0
	for c in text:
		if c == 'a':
			count = count + 1
	return count
	
print(countA("bananas"))


def countB(text):
	return text.count("a")
	
print(countB("bananas"))