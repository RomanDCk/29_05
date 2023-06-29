
lst = [0, 1, 0, 3, -12]
# lst = [0]
# lst = []
null = []
digits = []
for i in lst:
    if i != 0:
        digits.append(i)
    else:
        null.append(i)
digits.extend(null)
print(digits)
