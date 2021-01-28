# 5.3.2 List Comprehension

def gen_primes(max_val):
    """
    Generate list of prime numbers less than max_val
    """
    primes = []
    for x in range(2, max_val):
        is_prime = True
        for y in range(2, x):
            if x%y == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

def gen_primes_comprehension(max_val):
    """
    Generate list of prime numbers less than max_val
    using nested list comprehensions
    """
    # Use first comprehension to generate list of all candidate 
    # numbers [2..max_val], a second comprehension to generate list
    # of remainders of dividing a candidate prime by each potential divisor,
    # and the function 'all' to test if any of those remainders is 0
    return [x for x in range(2, max_val) if all(x % y != 0 for y in range(2, x))]

if __name__ == "__main__":
    # List of prime numbers up to 100
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    primes1 = gen_primes(100)
    assert primes1 == expected_primes
    
    primes2 =  gen_primes_comprehension(100)
    assert primes2 == expected_primes