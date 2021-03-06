# 12.2.1 Merge Sort

# Figure 12-5 Merge Sort
def merge(left, right, compare):
    """Assumes left and right are sorted lists and
         compare defines an ordering on the elements.
       Returns a new sorted (by compare) list containing the
         same elements as (left + right) would contain."""
    
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append remaining items in each list, if any
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering
         on elements of L
       Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

if __name__ == "__main__":
    L = [2,1,4,5,3]
    print(merge_sort(L), merge_sort(L, lambda x, y: x > y))

    # Finger exercise:
    # Use merge_sort to sort a list to tuples of integers.
    # The sorting order should be determined by the sum of the 
    # integers in the tuple.
    
    L = [(4, 5), (2, 3), (6, 7), (2, 8)]
    print(merge_sort(L, lambda x, y: sum(x) < sum(y)))
    # Sorted: [(2, 3), (4, 5), (2, 8), (6, 7)]
    
    L = [(4, 5, 6), (2, 3, 4), (6, 7, 8), (2, 6, 10)]
    print(merge_sort(L, lambda x, y: sum(x) < sum(y)))
    # Sorted: [(2, 3, 4), (4, 5, 6), (2, 6, 10), (6, 7, 8)]