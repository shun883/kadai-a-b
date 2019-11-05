# B-3
line = int(input('行列を入力してください: '))
column = int(input('列を入力してください: '))

for i in range(1, line + 1):

    for j in range(1, column + 1):
        print(f'{str(j).center(3)} × {str(i).center(3)} = {str(i * j).center(3)} | ', end=' ')
    print()
