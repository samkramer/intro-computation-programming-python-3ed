# 6.1 Fibonacci Numbers
# Figure 6-3: Recursive implementation of Fibonacci sequence

def fib_rec(n):
    """
    Assumes n int >= 0
    Returns Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
 
def fib_iter(n):
    """
    Assumes n int >= 0
    Returns Fibonacci of n
    """
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a + b
    return a
    
if __name__ == "__main__":
    n = 10
    
    print("Recursive Fibonacci:")
    for i in range(n+1):
        print(f"  fib({i}) = {fib_rec(i)}")
        
    print()
        
    print("Iterative Fibonacci:")
    for i in range(n+1):
        print(f"  fib({i}) = {fib_iter(i)}")
