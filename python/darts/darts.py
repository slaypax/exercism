from math import sqrt

def score(x, y):
    #some how this calculates the ditance from the center.
    # This is a math problem and unlikely to come up in an interview at amazon
    radius = sqrt(x * x + y * y)
    if radius > 10:
        return 0
    if radius > 5:
        return 1
    if radius > 1:
        return 5
    return 10
