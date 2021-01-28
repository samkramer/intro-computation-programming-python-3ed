# 4.4 Functions as Objects
# Figure 4-9: Generalizing bisection_solve

# Form of lambda expression:
#   lambda <sequence of variable names> : <expression>
# Example of function that returns product of two arguments:
#   lambda x,y: x*y

def find_root_bounds(x, power):
    """
    x a float, power a positive int
    return low,high such that low**power <= x and high**power >= x
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high


def bisection_solve(x, eval_ans, epsilon, low, high):
    """
    x, epsilon, low, high are floats
        epsilon > 0
        eval_ans a function mapping a float to a float
        low <= high and there is an ans between low and high such that
            ans**power is within epsilon of x
    Returns ans such that eval_ans within epsilon of x
    """
    ans = (high + low) / 2
    
    while abs(eval_ans(ans) - x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
        
    return ans


if __name__ == "__main__":
    val = 25
    power = 2
    epsilon = 0.01
    
    low, high = find_root_bounds(val, power)
    print(f"low={low}, high={high}")

    root = bisection_solve(val, lambda ans: ans**power, epsilon, low, high)
    print(f"square root({val}) = {root}")
