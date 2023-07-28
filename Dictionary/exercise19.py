#Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c': 300};
d2 = {'a': 300, 'b': 200, 'd': 400};

for k, v in d2.items():
    if k in d1:
        d1[k] += v;
    else:
        d1[k] = v;
print(d1)
