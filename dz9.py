import random

lst1 = []
lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 50))
print(lst)
lst1 = [lst[0], lst[2], lst[-2]]
print(lst1)
