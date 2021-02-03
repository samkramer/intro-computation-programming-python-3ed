# 5.7 Dictionaries
# Finger exercise: Implement a function that meets the specification

def get_min(d):
    """
    d is a dict mapping letters to ints
    Returns the value in d with the key that occurs first in the alphabet.
    Example:
        d = {x = 11, b = 12}
        get_min(d) returns 12
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for c in letters:
        if c in d.keys():
            return d[c]
        
if __name__ == "__main__":
    d = {'x':11, 'b':12}
    print(f"d = {d}")
    min_val = get_min(d)
    print(f"min_val = {min_val}")