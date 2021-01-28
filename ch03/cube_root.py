# 3.1 Exhaustive Enumeration
# Figure 3-1: Using exhaustive enumeration to find the cube root

# Find the cube root of a perfect cube

x = int(input('Enter an integer: '))

ans = 0
while ans**3 < x:
    ans = ans + 1
    
if ans**3 != x:
    print(f"{x} is not a perfect cube")
else:
    print(f"Cube root of {x} is {ans}")
