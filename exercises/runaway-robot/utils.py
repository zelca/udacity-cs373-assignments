from math import *


def angle_trunc(a):
    """This maps all angles to a domain of [-pi, pi]"""
    while a < 0.0:
        a += pi * 2
    return ((a + pi) % (pi * 2)) - pi


def get_heading(prev_position, next_position):
    """Returns the angle, in radians, between the target and hunter positions"""
    prev_x, prev_y = prev_position
    next_x, next_y = next_position
    heading = atan2(next_y - prev_y, next_x - prev_x)
    heading = angle_trunc(heading)
    return heading


# A helper function.
def distance_between(prev_position, next_position):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = prev_position
    x2, y2 = next_position
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
