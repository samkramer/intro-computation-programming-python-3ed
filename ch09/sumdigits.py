# 9.1 Handling Exceptions

# Finger exercise
def sum_digits(s):
    """
    Assumes s is a string
    Returns the sum of the decimal digits in s
        For example, if s is 'a2b3c' it returns 5
    """
    total = 0
    
    for c in s:
        # print(f"c: {c}")
        try:
            total += int(c)
        except ValueError:
            pass
    
    return total

if __name__ == "__main__":  
    print(f"sum_digits('a2b3c') = {sum_digits('a2b3c')}")
