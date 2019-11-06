"""
サイコロの面
サイコロをふる回数


"""

import random

dice_face = 8
dice_count = 3


def dice():
    count = 0
    while True:
        if count == dice_count:
            break
        print(random.randint(1, dice_face))
        count += 1


print(dice())
