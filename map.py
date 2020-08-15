li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def myfunc(x):
    return x**x


newlist = []

for item in li:
    newlist.append(myfunc(item))

print(newlist)

# using map
print(list(map(myfunc, li)))

# using list comprehension

print([myfunc(x) for x in li])

# using list comprehension and condition

print([myfunc(x) for x in li if x % 2 == 0])
