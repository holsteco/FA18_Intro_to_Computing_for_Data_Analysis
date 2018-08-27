def count_word_lengths(s):
	assert all([x.isalpha() or x == ' ' for x in s])
	assert type(s) is str
    #
	listofwords = s.split()
	listoflengths = []
	for length in listofwords:
		listoflengths.append(len(length))
	return listoflengths

    
    
#input
s = 'the quick  brown   fox jumped over     the lazy  dog' 
listoflengths = count_word_lengths

print(listoflengths)