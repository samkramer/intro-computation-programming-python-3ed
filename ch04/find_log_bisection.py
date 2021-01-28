# 4.4 Functions as Objects
# Figure 4-10: Using bisection_solve to approximate logs

# This function has been generalized to search for approximations
# to any monotonic function that maps floats to floats
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


def log(x, base, epsilon):
    """
    Assumes x and epsilon int or float, base an int,
        x > 1, epsilon > 0 and power >= 1
    Returns float y such that base**y is within epsilon of x
    """
    
    def find_log_bounds(x, base):
        upper_bound = 0
        while base**upper_bound < x:
            upper_bound += 1
        return upper_bound - 1, upper_bound
    
    low, high = find_log_bounds(x, base)
    print(f"low={low}, high={high}")
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)


if __name__ == "__main__":
    val = 36
    base = 2
    epsilon = 0.01
    
    ans = log(val, base, epsilon)
    print(f"{ans} is close to log base 2 of {val}")
