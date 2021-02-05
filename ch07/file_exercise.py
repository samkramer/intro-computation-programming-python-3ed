# 7.3 Files

# Finger exercise: 
# Write a program that first stores the first ten numbers
# in the Fibonnaci sequence to a file name 'fib_file'.
# Each number should be on a separate line in the file.
# The program should then read the numbers from the file
# and print them.

# Fibonacci (iterative implementation)
def fib(n):
    """
    Assumes n int >= 0
    Returns Fibonacci of n
    """
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    filename = 'fib_file.txt'

    # Write first 10 Fibonnaci numbers to file, one entry per line
    with open(filename, 'w') as out_file:
        n = 10
        for i in range(n+1):
            fib_i = fib(i)
            out_file.write(f"{fib_i}\n")
    
    # Read numbers from file and print them
    with open(filename, 'r') as in_file:
        for line in in_file:
            line = line.rstrip()
            print(line)
