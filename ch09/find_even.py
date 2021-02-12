# 9.2 Exceptions as a Control Flow Mechanism

# Finger exercise: implement a function that satisfies specification
def find_an_even(L):
    """
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number
    """
    for n in L:
        if n % 2 == 0:
            return n
    
    raise ValueError("List does not contain any even numbers")

if __name__ == "__main__":
    try:
        L1 = [1, 3, 5, 8, 9]
        print(f"First even number in {L1} is {find_an_even(L1)}")
        L2 = [1, 3, 5, 7, 9]
        print(f"First even number in {L2} is {find_an_even(L2)}")
    except ValueError as err:
        print(f"ValueError: {err}")
