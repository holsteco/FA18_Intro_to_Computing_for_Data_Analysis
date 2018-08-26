def strcat_list(L):
	assert type(L) is list
	L.reverse()
	Lc = "".join(L)
	return Lc

#the list	
L = ['jny', 'ags', 'uxp', 'qgf', 'iiu', 'dhq']

Lc = strcat_list(L)
print(Lc)
print(type(Lc))
print(type(L))