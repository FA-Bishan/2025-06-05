#this one takes a certain unit of time, and converts them into another unit.
import math


def MinToHour(minuite):
    hour = 0
    if (minuite < 60):
        hour = minuite/60
        return (f"{minuite} is {hour} hours.")
    else:
        hour = math.floor(minuite/60)
        remainingMins = minuite%60
        return (f"{minuite} is {hour} hours, and {remainingMins}mins.")
        