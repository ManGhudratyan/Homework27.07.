# Write a Python program to combine values in a list of dictionaries.
# Expected Output: Counter({'item1': 1150, 'item2': 300})

ml = [
        {'item': 'item1', 'amount': 400}, 
        {'item': 'item2', 'amount': 300}, 
        {'item': 'item1', 'amount': 750}
    ]

md = {};

for el in ml:
    item = el['item'];
    amount = el['amount'];
    if item in md:
        md[item] += amount;
    else:
        md[item] = amount;
print(md)