# 3.4 Newton-Raphson
# Figure 3-7: Implementation of Newton-Raphson method
# Newton-Raphson for square root

# Sample output:
# Enter a number: 25
# Number of guesses = 4
# Square root of 25 is about 5.000012953048684

k = int(input('Enter a number: '))

epsilon = 0.01
num_guesses = 0
guess = k / 2

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    num_guesses += 1

print(f"Number of guesses = {num_guesses}")
print(f"Square root of {k} is about {guess}")