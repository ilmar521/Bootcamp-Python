import math
import random
import re
import traceback


def calc_angle(time):
    list_of_clock = time.split(':')
    hours = int(list_of_clock[0])
    minutes = int(list_of_clock[1])
    if hours > 12:
        hours -= 12
    ans = abs((hours * 30 + minutes * 0.5) - (minutes * 6))
    return min(360 - ans, ans)

print(calc_angle('14:18'))
print(calc_angle('00:00'))
print(calc_angle('23:59'))
print(calc_angle('5:15'))