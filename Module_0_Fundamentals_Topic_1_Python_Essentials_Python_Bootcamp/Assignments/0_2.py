

def strcat_ba(a, b):
    assert type(a) is str
    assert type(b) is str
    result = b + a
    return result

a = "5"
b = "3"

result = strcat_ba(a, b)

#why doesn't print(result = strcat_ba(a, b)) work??