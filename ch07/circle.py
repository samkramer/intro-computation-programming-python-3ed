# 7.1 Modules
# Figure 7-1: Some code relatd to circles and spheres

pi = 3.14159

def area(radius):
    return pi * (radius**2)

def circumference(radius):
    return 2 * pi * radius

def sphere_surface(radius):
    return 4.0 * area(radius)

def sphere_volume(radius):
    return (4 / 3) * pi * (radius**3)

