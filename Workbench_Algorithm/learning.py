a = 3
b = a

store = id(a)
print(store)

c = complex(a+b, b)
print(c)
print(type(c))


# vision = range(1, 10)
vision = list(range(11))
print(vision)


data_set = (23, 34, 56, 67, 78, 89, 10, 11, 12, 56)
# check_set = data_set.count(56)
check_set = data_set.index(56)
# data_set.extend([4,3,7,1,2,13])
# data_set.sort()
# data_set.index(1)
print(data_set)
print(check_set)

d = {'Rahul':'IphoneSE 4', 'Kiran':'Iphone5', 'Abu':'Iphone11'}
# d_values = d.values()
# d_keys = d.keys()
# print(d_values)
# print(d_keys)
d_get = d.get('Rahul')
print(d_get)
