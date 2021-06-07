# 15.2 Dynamic Programming and the 0/1 Knapsack Problem
import random
import string

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
        
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        result = ('<' + self.name + ', ' + str(self.value)
                 + ', ' + str(self.weight) + '>')
        return result


# Figure 15-5: Using a decision tree to solve a knapsack problem
def max_val(to_consider, avail):
    """Assumes to_consider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    
    if not to_consider or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        # Explore right branch only
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        
        # Explore left branch
        with_val, with_to_take = max_val(to_consider[1:],
                                         avail - next_item.get_weight())
        with_val += next_item.get_value()
        
        # Explore right branch
        without_val, without_to_take = max_val(to_consider[1:], avail)
        
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    
    return result


# Figure 15-7: Dynamic programming solution to knapsack problem
def fast_max_val(to_consider, avail, memo = {}):
    """Assumes to_consider a list of items, avail a weight,
         memo supplied by recursive calls to keep track of solutions
         to sub-problems that have already been solved.
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
         
    # The expression len(to_consider) is a compact way of representing
    # items still to be considered. This works because items are always
    # removed from the same end (front) of the list to_consider.
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif not to_consider or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        # Explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        
        # Explore left branch
        with_val, with_to_take = fast_max_val(to_consider[1:],
                                              avail - next_item.get_weight(),
                                              memo)
        with_val += next_item.get_value()
        
        # Explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:],
                                                    avail, memo)
        
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
            
    memo[(len(to_consider), avail)] = result
    return result


def print_items(items):
    print('Items:')
    for item in items:
        print(item)
    print()

    
def print_items_taken(items_taken, total_val):
    print('Items Taken:')
    for item in items_taken:
        print(item)
    print('Total value of items taken =', total_val)

        
# Figure 15-6 on page 314
def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    print_items(Items)
        
    val, taken = max_val(Items, 5)
    print_items_taken(taken, val)


def build_many_items(num_items, max_val, max_weight):
    letters = string.ascii_uppercase
    letters_count = len(letters)
    
    items = []
    for i in range(num_items):
        idx = i % letters_count
        item_label = f"{letters[idx]}{i+1}"
        items.append(Item(item_label,
                          random.randint(1, max_val),
                          random.randint(1, max_weight)))
    return items


def big_test(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    print_items(items)
    
    val, taken = max_val(items, avail_weight)
    print_items_taken(taken, val)
    
    
def big_test_dynamic(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    print_items(items)
    
    val, taken = fast_max_val(items, avail_weight)
    print_items_taken(taken, val)

    
if __name__ == "__main__":
    # small_test()
    # big_test(10, 40)
    big_test_dynamic(40, 100)
    