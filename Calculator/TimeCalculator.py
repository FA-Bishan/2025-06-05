#this one takes a certain unit of time, and converts them into another unit.
import math


def MinToHour(minuite):
    hour = 0
    if (int(minuite) < 60):
        hour = minuite/60
        return hour, 0
    else:
        hour = math.floor(int(minuite)/60)
        remainingMins = int(minuite)%60
        return hour, remainingMins