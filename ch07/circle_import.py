# 7.1 Modules

import circle

pi = 3.14
print(f"pi={pi}")

print()
print("The following are from imported module 'circle':")

print(f"pi={circle.pi}")
print(f"area={circle.area(3)}")
print(f"circumference={circle.circumference(3)}")
print(f"sphere_surface={circle.sphere_surface(3)}")
