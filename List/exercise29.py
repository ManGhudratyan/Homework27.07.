# Write a Python program to get unique values from a list.

ml = [10, 20, 30, 40, 20, 50, 60, 40];
new_ml = [];

for el in ml:
    if el not in new_ml:
        new_ml.append(el);
print(new_ml)