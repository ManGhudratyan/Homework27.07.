#Write a Python program to get the top three items in a shop.

items = {
        'item1' : 45.50, 
        'item2': 35, 
        'item3': 41.30, 
        'item4': 55, 
        'item5': 24
};

mlist = list(items.items());

for i in range(0, len(mlist)):
    for j in range(0, len(mlist) - 1 - i):
        if mlist[j][1] < mlist[j + 1][1]:
            mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]
print(mlist[:3]);

