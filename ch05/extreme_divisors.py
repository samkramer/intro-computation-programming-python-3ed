# 5.1.1 Multiple Assignment

def find_extreme_divisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints
    Returns tuple containing smallest common divisor > 1 and
        largest common divisor of n1 and n2. If no common
        divisor, other than 1, returns (None, None)
    """
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

if __name__ == "__main__":
    min_divisor, max_divisor = find_extreme_divisors(100, 200)
    print(f"min_divisor = {min_divisor}, max_divisor = {max_divisor}")
    # Output:
    # min_divisor = 2, max_divisor = 100