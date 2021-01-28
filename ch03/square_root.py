# 3.2 Approximate Solutions and Bisection Search
# Figure 3-4: Approximating square root using exhaustive enumeration

# Sample output:
# Enter a number: 25
# Number of guesses = 49990
# 4.999000000001688 is close to the square root of 25.0

x = float(input('Enter a number: '))

epsilon = 0.01
step = epsilon ** 2
num_guesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
    
print(f"Number of guesses = {num_guesses}")

if abs(ans**2 -x) >= epsilon:
    print(f"Failed on square root of {x}")
else:
    print(f"{ans} is close to the square root of {x}")