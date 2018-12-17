def ret_list():
    ll = [1,2]
    return ll

x = ret_list()
y = ret_list()
print id(x) == id(y) #False
