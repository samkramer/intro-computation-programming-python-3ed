# 3.2 Approximate Solutions and Bisection Search
# Figure 3-6: Using bisection search to estimate log base 2

# Sample output:
# Enter a number: 36
# lower_bound = 6
# 5.169921875 is close to log base 2 of 36

x = int(input('Enter a number: '))

# Find lower bound
lower_bound = 0
while 2**lower_bound < x:
    lower_bound += 1
print(f"lower_bound = {lower_bound}")

low = lower_bound - 1
high = lower_bound + 1
epsilon = 0.01

# Perform bisection search
ans = (high + low) / 2
while abs(2**ans - x) >= epsilon:
    if 2**ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
    
    
print(f"{ans} is close to log base 2 of {x}")