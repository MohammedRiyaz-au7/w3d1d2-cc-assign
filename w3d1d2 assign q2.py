from collections import Counter
d1 = {'a': 300, 'b': 100, 'c':700}
d2 = {'a': 200, 'b': 500, 'd':800}
d = Counter(d1) + Counter(d2)
print(d)
