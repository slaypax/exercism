def equilateral(sides):
    sides = sorted(sides)
    x, y, z = sides
    return x == y and y == z and x != 0

def isosceles(sides):
    sides = sorted(sides)
    x, y, z = sides
    return (x == y or y == z or z == x) and (x + y) > z


def scalene(sides):
    sides = sorted(sides)
    x, y, z = sides
    return (x != y and x !=z and y != z) and (x + y) > z
