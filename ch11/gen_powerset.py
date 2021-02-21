# 11.3.6 Exponential Complexity

# Figure 11-6 from page 227
def get_binary_rep(n, num_digits):
   """Assumes n and numDigits are non-negative ints
      Returns a str of length numDigits that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > num_digits:
      raise ValueError('not enough digits')
   for i in range(num_digits - len(result)):
      result = '0' + result
   return result

def gen_powerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L. E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      bin_str = get_binary_rep(i, len(L))
      subset = []
      for j in range(len(L)):
         if bin_str[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset

if __name__ == "__main__":
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    print(gen_powerset(letters[0:3]))
    # [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
    
    print(len(gen_powerset(letters[0:10])))     # 1024
    print(len(gen_powerset(letters[0:20])))     # 1048576