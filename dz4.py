x = float(input('Type x: '))
action = input('Type action: ')
y = float(input('Type y: '))
if action == '+':
    print(x + y)
elif action == '-':
    print(x - y)
elif action == '*':
    print(x * y)
elif action == '/':
    if y == 0:
        print('Zero devision error')
    else:
        print(x / y)