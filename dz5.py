
#lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
lst = []
size = len(lst)
m = size // 2
if size % 2 != 0:
    m +=1
print([lst[:m], lst[m:]])