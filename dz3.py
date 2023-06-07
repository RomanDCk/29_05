x = int(input('Type int5x: '))
# /10000
y = 10000
digit = x
left, right = divmod(digit, y)
p = (left)

# /1000
z = 1000
digit = right
left, right = divmod(digit, z)
o = (left)

# /100
f = 100
digit = right
left, right = divmod(digit, f)
i = (left)

# /10
d = 10
digit = right
left, right = divmod(digit, d)
u = (left)
# / 1
h = 1
digit = right
left, right = divmod(digit,h)
r = (left)
print(r,u,i,o,p)

