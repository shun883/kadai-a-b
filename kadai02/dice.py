"""
サイコロの面
サイコロをふる回数


"""

import random

dice_face = int(input('サイコロの面の数は？'))
dice_count = int(input('何回振りますか？'))


def dice():
    count = 0
    dice_list = list()
    while True:
        if count == dice_count:
            break
        dice_list.append(random.randint(1, dice_face))
        count += 1
    print(dice_list)

dice()
