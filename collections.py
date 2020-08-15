import collections
from collections import Counter

c = Counter('gallad')
print(c)
d = Counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(d)
e = Counter({'a': 2, 'b': 4, 'c': 16})
print(e)

print(list(e.elements()))


print(e.most_common(1)[0][0], e.most_common(1)[0][1])
