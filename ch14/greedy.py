# 14.1.1 Greedy Algorithms

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

# Figure 14-3 Implementation of a greedy algorithm
def greedy(items, max_weight, key_function):
    """Assumes items a list, max_weight >= 0,
       key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    print_items(items_copy, f"Sorted list of items by {key_function.__name__}:")
    
    result = []
    total_value = 0.0
    total_weight = 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)

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

def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print_items(taken, f"Total value of items taken is {val}")       

def test_greedys(max_weight = 20):
    items = build_items()
    print_items(items, "Original list of items:")
    
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    
    print('Use greedy by weight to fill knapsack of size',
          max_weight)
    test_greedy(items, max_weight, weight_inverse)
    
    print('Use greedy by density to fill knapsack of size',
          max_weight)
    test_greedy(items, max_weight, density)
    
if __name__ == "__main__":
    test_greedys()
    