# 12.2 Sorting Algorithms

# Figure 12-4 Selection sort
def sel_sort(L):
    """Assumes that L is a list of elements that can be
         compared using >.
       Sorts L in ascending order"""
    for suffix_start in range(len(L)):
        # look at each element in suffix
        for i in range(suffix_start+1, len(L)):
            if L[i] < L[suffix_start]:
                # swap position of elements
                L[suffix_start], L[i] = L[i], L[suffix_start]
        
        
if __name__ == "__main__":
    lst = [7, 6, 10, 5, 9, 8, 4, 1, 3, 2]
    print(lst)
    
    sel_sort(lst)
    print(lst)