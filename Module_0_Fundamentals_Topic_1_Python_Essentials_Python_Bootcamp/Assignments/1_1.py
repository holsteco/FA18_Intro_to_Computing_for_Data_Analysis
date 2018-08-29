#corey b. holstege
#2018-08-29

def remove_all(L, x):
    assert type(L) is list and x is not None
    #
    # YOUR CODE HERE
    #
    #copy list
    newlist = L[:]
    #exclude (delete) x from the list
    for item in range(newlist.count(x)):
        newlist.remove(x)
    return newlist
    
#inputs to function    
L = ([1, 2, 3, 2, 4, 8, 2], 2)
x = 2