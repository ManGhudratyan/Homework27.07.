# Write a Python program to find the second largest number in a list.

ml = [20, 40, 10, 50, 70, 30];

for i in range(0, len(ml)):
    for j in range(len(ml) - i - 1):
        if (ml[j] < ml[j + 1]):
            ml[j], ml[j + 1] = ml[j + 1], ml[j];
print(ml[1])