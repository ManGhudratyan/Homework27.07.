# Write a Python program to get the frequency of elements in a list

ml = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30];
new_ml = {};

for i in ml:
    if i in new_ml:
        new_ml[i] += 1;
    else:
        new_ml[i] = 1;
print(new_ml)