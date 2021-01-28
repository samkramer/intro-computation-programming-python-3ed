# 5.4 Higher-Order Operations on LIsts

def apply_to_ach(L, f):
    """
    Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])
        
def exercise(L1, L2):
    """
    L1, L2 are lists of same length of numbers
    Returns sum of raising each element in L1
        to the power of element at same index in L2
    Examples:
        f([1,2], [2,3]) returns 9
        f([2,3], [3,4]) returns 89
    """
    L3 = list(map(lambda x,y: x**y, L1, L2))
    return sum(L3)


if __name__ == "__main__":
    L = [1, -2, 3.33]
    print(f"L = {L}")
    
    print()
    print('Apply abs to each element of list')
    apply_to_ach(L, abs)
    print(f"L = {L}")
    
    print()
    print('Apply int to each element of list')
    apply_to_ach(L, int)
    print(f"L = {L}")
    
    print()
    print('Apply squaring to each element of list')
    apply_to_ach(L, lambda x: x**2)
    print(f"L = {L}")
    
    # Example using built-in higher order function 'map'
    # with unary function (function with one parameter)
    print()
    print('Use map to square each element in list')
    L = [2, 4, 6]
    L = list(map(lambda x: x**2, L))
    print(L)
    
    # Apply map in a for loop
    print()
    print('Use map in for loop to square each element in list')
    L = [2, 4, 6]
    for i in map(lambda x: x**2, L):
        print(i)
        
    # Apply map to multiple collections
    # Note: each collection must have same length
    print()
    print('Use map in for loop to find min value of each element in two lists')
    L1 = [1, 28, 36]
    L2 = [2, 57, 9]
    for i in map(min, L1, L2):
        print(i)
    
    # Finger exercise
    print()
    print('Test for finger exercise')
    L1 = [1, 2]
    L2 = [2, 3]
    print(f"exercise({L1}, {L2},) = {exercise(L1, L2)}")
    L1 = [2, 3]
    L2 = [3, 4]
    print(f"exercise({L1}, {L2},) = {exercise(L1, L2)}")
    