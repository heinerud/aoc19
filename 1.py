import sys
import math


def weight(x):
    return int(math.floor(x / 3) - 2)


def fuel(x, fuels=None):
    if fuels is None:
        fuels = []
    res = weight(x)
    if res <= 0:
        return sum(fuels)
    else:
        fuels.append(res)
        return fuel(res, fuels)


input = [int(x) for x in sys.argv[1:]]
print(sum([weight(x) for x in input]))
print(sum([fuel(x) for x in input]))
