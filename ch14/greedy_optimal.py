# 14.1.2 An Optimal Solution to the 0/1 Knapsack Problem

# Figure 14-2 from page 284
class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w
        
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value
    
    def get_weight(self):
        return self._weight
    
    def __str__(self):
        return f'<{self._name}, {self._value}, {self._weight}>'

def value(item):
    return item.get_value()

def weight_inverse(item):
    return 1.0 / item.get_weight()

def density(item):
    return item.get_value() / item.get_weight()


# Figure 14-4 Using a greedy algorithm to choose items
def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def print_items(items, label):
    print(label)
    for item in items:
        print('   ', item)
    print()

# # Code from Figure 11-6
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

# # Figure 14-5 on page 289
def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)

def test_best(max_weight = 20):
    items = build_items()
    pset = gen_powerset(items)
    print(f"Number of sets generated: {len(pset)}")
        
    taken, val = choose_best(pset, max_weight, Item.get_value,
                             Item.get_weight)
    print_items(taken, f"Total value of items taken is {val}")

    
if __name__ == "__main__":
    test_best()
    