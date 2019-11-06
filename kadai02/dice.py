"""
サイコロの面
サイコロをふる回数


"""

import random

dice_face = int(input('サイコロの面の数は？'))
dice_count = int(input('何回振りますか？'))


def dice():
    count = 0
    while True:
        if count == dice_count:
            break
        print(random.randint(1, dice_face))
        count += 1


dice()
