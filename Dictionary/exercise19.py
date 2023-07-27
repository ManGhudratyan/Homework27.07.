#Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a' : 100, 'b' : 200, 'c' : 300};
d2 = {'a' : 300, 'b' : 200, 'd' : 400};
d3 = {};

for k,v in d1.items():
    if k in d3:
        d3[k] += v;
    else:
        d3[k] = v;

for k,v in d2.items():
    if k in d3:
        d3[k] += v;
    else:
        d3[k] = v;
print(d3)
