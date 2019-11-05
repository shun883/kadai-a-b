# B-1
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print()

# B-2
line = int(input('行列を入力してください: '))
column = int(input('列を入力してください: '))

for i in range(1, line + 1):
    for j in range(1, column + 1):
        print(i * j, end=' ')
    print()

# B-3
line = int(input('行列を入力してください: '))
column = int(input('列を入力してください: '))

for i in range(1, line + 1):
    for j in range(1, column + 1):
        print(f'{i} × {j} = {i * j} | ', end=' ')
    print()
