# 5.1 Tuples

def intersect(t1, t2):
    """
    Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in both t1 and t2
    """
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

if __name__ == "__main__":
    tup1 = (1, 'a', 2)
    tup2 = ('b', 2, 'a')
    print(intersect(tup1, tup2))    # ('a', 2)
    