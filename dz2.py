
x = int(input('Type int: '))
# /1000
y = 1000
digit = x
left, right = divmod(digit, y)
print(left)

# /100
z = 100
digit = right
left, right = divmod(digit, z)
print(left)

# /10
f = 10
digit = right
left, right = divmod(digit, f)
print(left)

# /1
d = 1
digit = right
left, right = divmod(digit, d)
print(left)









