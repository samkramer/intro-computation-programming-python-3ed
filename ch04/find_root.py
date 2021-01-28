# 4.1 Functions and Scoping

# Figure 4-3: A function for finding roots
def find_root(x, power, epsilon):
    """
    Assumes x and epsilon are of type int or float,
        power of type int, 
        epsilon > 0 and power >= 1
    Returns float y such that y**power is within epsilon of x,
        If such a float does not exist, it returns None
    """
    
    if x < 0 and power%2 == 0:
        # Negative number has no even-powered roots
        return None
    
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2
    
    while abs(ans**power - x) >= epsilon:
        # print(f"low={low}, high={high}, ans={ans}")
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
        
    return ans


# Figure 4-4: Code to test find_root
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
    # x = int(input('Enter a number: '))
    # root = find_root(x, 3, 0.01)
    # print(f"{root} is close to cube root of {x}")
    
    x_vals = (0.25, 8, -8)
    powers = (1, 2, 3)
    epsilons = (0.1, 0.01, 0.001)
    test_find_root(x_vals, powers, epsilons)
    
    print()
    help(find_root)