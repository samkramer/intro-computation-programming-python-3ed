# Chapter 6.3 Global Variables
# Figure 6-6: Using a global variable

def fib(x):
    """Assumes x an int >= 0
       Returns Fibonacci of x"""
    global num_fib_calls
    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib(n):
    for i in range(n+1):
        global num_fib_calls
        num_fib_calls = 0
        print('fib of', i, '=', fib(i))
        print('  fib called', num_fib_calls, 'times')
        
if __name__ == "__main__":
    test_fib(10)