# 11.3.5 Polynomial Complexity

# Figure 11-4 from page 225
def is_subset(L1, L2):
   """Assumes L1 and L2 are lists.
      Returns True if each element in L1 is also in L2
      and False otherwise."""
   for e1 in L1:
      matched = False
      for e2 in L2:
         if e1 == e2:
            matched = True
            break
      if not matched:
         return False
   return True

if __name__ == "__main__":
    L1 = [1, 3, 5, 7, 9]
    L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(is_subset(L1,L2))
    L1 = [1, 3, 5, 7, 11, 9]
    print(is_subset(L1,L2))
