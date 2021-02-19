# 10.1 Abstract Data Types and Classes

# Figure 10-1 from page 182
class Int_set(object):
    """An Int_set is a set of integers"""
    #Information about the implementation (not the abstraction):
      #Value of a set is represented by a list of ints, self._vals.
      #Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self._
           Nothing can be assumed about the order of the elements"""
        return self._vals[:]
    
    # Finger exercise
    def union(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the elemnts in self
        plus the elements in other.
        """
        other_vals = other.get_members()
        for e in other_vals:
            if e not in self._vals:
                self._vals.append(e)
                
    # Finger exercise, use + operator to denote set union
    def __add__(self, other):
        new_set = Int_set()
        new_set._vals = self._vals[:]
        new_set.union(other)
        return new_set

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
    
# Finger exercise test for union() method
def test_union():
    # a = {1,2}
    a = Int_set()
    a.insert(1)
    a.insert(2)
    
    # b = {2,3,4}
    b = Int_set()
    b.insert(2)
    b.insert(3)
    b.insert(4)
    
    # a ∪ b = {1,2,3,4}
    a.union(b)
    print(a)
    
# Finger exercise test for __add__ union method
def test_union_plus_operator():
    # a = {1,2}
    a = Int_set()
    a.insert(1)
    a.insert(2)
    
    # b = {2,3,4}
    b = Int_set()
    b.insert(2)
    b.insert(3)
    b.insert(4)
    
    # c = a ∪ b = {1,2,3,4}
    c = a + b
    print(c)
    
  
if __name__ == "__main__": 
    s = Int_set()
    s.insert(3)
    print(s.member(3))
    
    print()
    
    s = Int_set()
    s.insert(3)
    s.insert(4)
    print(str(s))
    print('The value of s is', s)
    
    print()
    
    test_union()
    
    print()
    
    test_union_plus_operator()
