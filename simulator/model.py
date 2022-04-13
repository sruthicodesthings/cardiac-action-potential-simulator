import math


def smooth_step(start, end, points):
    """Makes the line less blocky between two voltages."""
    values = []
    for i in range(points):
        x = i / max(points - 1, 1)
        s = x * x * (3 - 2 * x)
        values.append(start + (end - start) * s)
    return values
