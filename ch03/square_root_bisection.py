# 3.2 Approximate Solutions and Bisection Search
# Figure 3-5: Using bisection search to approximate square root

# Sample output:
# Enter a number: 25
# low=0, high=25, ans=12.5
# low=0, high=12.5, ans=6.25
# low=0, high=6.25, ans=3.125
# low=3.125, high=6.25, ans=4.6875
# low=4.6875, high=6.25, ans=5.46875
# low=4.6875, high=5.46875, ans=5.078125
# low=4.6875, high=5.078125, ans=4.8828125
# low=4.8828125, high=5.078125, ans=4.98046875
# low=4.98046875, high=5.078125, ans=5.029296875
# low=4.98046875, high=5.029296875, ans=5.0048828125
# low=4.98046875, high=5.0048828125, ans=4.99267578125
# low=4.99267578125, high=5.0048828125, ans=4.998779296875
# low=4.998779296875, high=5.0048828125, ans=5.0018310546875
# Number of guesses = 13
# 5.00030517578125 is close to square root of 25

x = int(input('Enter a number: '))

epsilon = 0.01
num_guesses = 0

low = 0
high = max(1, x)
ans = (high + low) / 2

while abs(ans**2 - x) >= epsilon:
    print(f"low={low}, high={high}, ans={ans}")
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
    
    
print(f"Number of guesses = {num_guesses}")
print(f"{ans} is close to square root of {x}")
    