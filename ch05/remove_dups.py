# 5.3.1 Cloning

def remove_dups(lst1, lst2):
    """
    Assumes that lst1 and lst2 are lists
    Removes any element from lst1 that also occurs in lst2
    """
    for e1 in lst1[:]:  # use slicing to clone
        if e1 in lst2:
            lst1.remove(e1)

if __name__ == "__main__":
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups(L1, L2)
    print(L1)   # [3, 4]
