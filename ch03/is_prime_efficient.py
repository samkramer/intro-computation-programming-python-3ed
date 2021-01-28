# 3.1 Exhaustive Enumeration
# Figure 3-3: A more efficient primality test

# Test if input > 2 is a prime number.
# If not, print smallest divisor
# This implementation eliminates checking of even numbers beyond 2

x = int(input('Enter an integer greater than 2: '))

smallest_divisor = None
if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            smallest_divisor = guess
            break

if smallest_divisor != None:
    print(f"Smallest divisor of {x} is {smallest_divisor}")
else:
    print(f"{x} is a prime number")