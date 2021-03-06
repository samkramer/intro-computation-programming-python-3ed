# 12.1 Search Algorithms


# Figure 12-3: Recursive binary search
def search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    
    def bin_search(L, e, low, high):
        if high == low:
            return L[low] == e
        
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bin_search(L, e, low, mid - 1)
        else:
            return bin_search(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)

    
if __name__ == "__main__":
    lst = list(range(3,16))
    print(lst)
    
    elem = 12
    print(f"{elem} in list: {search(lst, elem)}")
    
    elem = 16
    print(f"{elem} in list: {search(lst, elem)}")