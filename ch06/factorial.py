# 6.0 Recursion
# Figure 6-1: Iterative and recursive implementations of factorial

# Iterative solution of factorial
def fact_iter(n):
    """
    Assumes n an int > 0
    Returns n!
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Recursive solution of factorial
def fact_rec(n):
    """
    Assumes n an int > 0
    Returns n!
    """
    if n == 1:
        return 1
    return n * fact_rec(n-1)

# Finger exercise
def harmonic(n):
    """
    Assumes n an int > 0
    Returns 1 + 1/2 + 1/3 + ... + 1/n
    """
    if n == 1:
        return 1
    return (1/n) + harmonic(n-1)
    

if __name__ == "__main__":
    n = 5
    print(f"(iteration) {n}! = {fact_iter(n)}")
    print(f"(recursion) {n}! = {fact_rec(n)}")
    
    print()
    
    # Finger exercise
    n = 20
    print(f"harmonic({n}) = {harmonic(n)}") # harmonic(20) = 3.597739657143682
