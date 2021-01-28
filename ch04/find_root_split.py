# 4.3 Using Functions to Modularize Code
# Figure 4-8: Splitting find_root into multiple functions

def find_root_bounds(x, power):
    """
    x a float, power a positive int
    return low,high such that low**power <= x and high**power >= x
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """
    x, epsilon, low, high are floats
        epsilon > 0
    low <= high and there is an ans between low and high such that
        ans**power is within epsilon of x
    Returns ans such that ans**power within epsilon of x
    """
    ans = (high + low) / 2
    
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
        
    return ans

def find_root(x, power, epsilon):
    """
    Assumes x and epsilon int or float, power an int,
        epsilon > 0 and power >= 1
    Returns float y such that y**power is within epsilon of x.
        If such float does not exist, return None
    """
    
    if x < 0 and power%2 == 0:
        # Negative number has no even-powered roots
        return None
    
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)


def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result is None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:
                        val = 'Bad'
                print(f"x = {x}, power = {p}, epsilon = {e}: {val}")


if __name__ == "__main__":
    x_vals = (0.25, 8, -8)
    powers = (1, 2, 3)
    epsilons = (0.1, 0.01, 0.001)
    test_find_root(x_vals, powers, epsilons)
    