# A-1
users = ['Bob', 'Tom', 'Ken']

# A-2
int_number = [1, 2, 3, 4, 5]

# A-3
kazuma_info = ['Kazuma', 'Takahashi', 35]

# A-4
members = ['Kazuma', 'Makoto', 'Ohira']
print(members[0], members[1])

# A-5
print(f'Name: {kazuma_info[1]} {kazuma_info[0]},Age:{kazuma_info[2]}')

# A-6
odd_numbers = [1, 3, 5, 7, 9]
for o_num in odd_numbers:
    print(o_num)

# A-7
even_numbers = [2, 4, 6, 8]
for e_num in even_numbers:
    print(e_num * 2)

# A-8
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

for user_info in users_info:
    print(f'Name: {user_info[0]}, Age: {user_info[1]}')

# A-9
kazuma_info = {'first_name': 'kazuma', 'family_name': 'takahashi', 'age': 35}

print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35


# A-10
import random

def dice():
    print(random.randint(1, 6))

dice()

# A-11
height = float(input('Height(m)? >'))
weight = float(input('Weight(kg) >'))

bmi = weight / (height ** 2)

print(f'Your BMI is {round(bmi, 2)}')
