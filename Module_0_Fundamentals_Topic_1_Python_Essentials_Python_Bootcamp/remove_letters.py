#li = ([1, 2, 3, 2, 4, 8, 2], 2)
#this = 2

#def removeThis(li, this):
	#for item in range(li.count(this)):
		#li.remove(this)
	#return li

#print(li)



x = [1, 1, 1, 1, 1, 1, 2, 3, 2]
z = 1

def removeThis(x, z):
	#a = x[:]
	for item in range(x.count(z)):
		x.remove(z)
	return x

#a = x	
#print (removeThis)
#print(a)

for item in range(x.count(z)):
	x.remove(z)
	
print(x)